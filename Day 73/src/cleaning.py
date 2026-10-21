"""
cleaning.py - Day 73: clean the Stack Overflow programming language data.

Input : ../data/raw/QueryResults.csv  (columns: date, tag name, number of posts)
Output: ../data/processed/posts_long.csv   (DATE, TAG, POSTS - one row per month/language)
        ../data/processed/posts_pivot.csv  (DATE rows x TAG columns, ready to plot)
"""

from pathlib import Path

import pandas as pd

RAW_PATH = Path("../data/raw/QueryResults.csv")
CLEAN_DIR = Path("../data/processed")


def load_data(path: Path = RAW_PATH) -> pd.DataFrame:
    # The file has its own header row (m, TagName, Unnamed: 2), so replace it
    return pd.read_csv(path, names=["DATE", "TAG", "POSTS"], header=0)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Trim whitespace and standardise the tag names
    df["TAG"] = df["TAG"].astype(str).str.strip().str.lower()

    # Convert date strings to real datetimes
    df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")

    # Post counts should be numeric
    df["POSTS"] = pd.to_numeric(df["POSTS"], errors="coerce")

    # Drop rows missing any key field, and exact duplicates
    df = df.dropna(subset=["DATE", "TAG", "POSTS"])
    df = df.drop_duplicates(subset=["DATE", "TAG"])

    df["POSTS"] = df["POSTS"].astype(int)
    return df.sort_values(["DATE", "TAG"]).reset_index(drop=True)


def make_pivot(df: pd.DataFrame) -> pd.DataFrame:
    """One column per language; months with no posts become 0 instead of NaN."""
    pivot = df.pivot(index="DATE", columns="TAG", values="POSTS")
    return pivot.fillna(0).astype(int)


def report(df: pd.DataFrame, pivot: pd.DataFrame) -> None:
    print(f"Clean data: {df.shape[0]} rows x {df.shape[1]} cols")
    print(f"Date range: {df['DATE'].min().date()} to {df['DATE'].max().date()}")
    print(f"Languages ({df['TAG'].nunique()}): {', '.join(sorted(df['TAG'].unique()))}")
    print("\nMonths of data per language:")
    print(df.groupby("TAG")["DATE"].count().sort_values(ascending=False).to_string())
    print("\nTotal posts per language:")
    print(df.groupby("TAG")["POSTS"].sum().sort_values(ascending=False).to_string())
    print(f"\nPivot shape: {pivot.shape}")
    print(pivot.head())


if __name__ == "__main__":
    raw = load_data()
    df = clean_data(raw)
    pivot = make_pivot(df)
    report(df, pivot)

    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_DIR / "posts_long.csv", index=False)
    pivot.to_csv(CLEAN_DIR / "posts_pivot.csv")
    print(f"\nSaved cleaned files to {CLEAN_DIR}/")
