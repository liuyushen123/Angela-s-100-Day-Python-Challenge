from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = ROOT / "data" / "raw" / "salaries_by_college_major.csv"
PROCESSED_PATH = ROOT / "data" / "processed" / "salaries_clean.csv"


def load_raw(path=RAW_PATH) -> pd.DataFrame:
    """Load the original CSV without modifying it."""
    return pd.read_csv(path)


def drop_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with NaN values (the file has a junk row at the bottom)."""
    return df.dropna().reset_index(drop=True)


def add_spread(df: pd.DataFrame) -> pd.DataFrame:
    """Add the 90th-10th percentile spread as a proxy for career 'risk'."""
    df = df.copy()
    df["Spread"] = (
        df["Mid-Career 90th Percentile Salary"]
        - df["Mid-Career 10th Percentile Salary"]
    )
    return df


def add_growth(df: pd.DataFrame) -> pd.DataFrame:
    """Add % salary growth from starting to mid-career."""
    df = df.copy()
    df["Growth %"] = (
        (df["Mid-Career Median Salary"] - df["Starting Median Salary"])
        / df["Starting Median Salary"]
        * 100
    )
    return df


def get_clean_data(save=False) -> pd.DataFrame:
    """Run the full pipeline: load -> drop NaNs -> add derived columns."""
    df = load_raw().pipe(drop_missing).pipe(add_spread).pipe(add_growth)
    if save:
        PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(PROCESSED_PATH, index=False)
    return df


if __name__ == "__main__":
    get_clean_data(save=True)
    print(f"Saved to {PROCESSED_PATH}")
