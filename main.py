import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

# Set the random seed for reproducibility
random.seed(0)
np.random.seed(0)

num_rows = 100  # Number of rows in the DataFrame

# Random dates for dataframe
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = [
    start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    for _ in range(num_rows)
]

# Random product IDs in a defined format (e.g., 'P001', 'P002', ..., 'P010')
product_ids = [f"P{str(random.randint(1, 10)).zfill(3)}" for _ in range(num_rows)]

# Random number of units sold (e.g., between 1 and 100)
units_sold = [random.randint(1, 100) for _ in range(num_rows)]

# Create the DataFrame
df = pd.DataFrame(
    {"Date": date_range, "Product_ID": product_ids, "Units_Sold": units_sold}
)

df.head()


def most_sold_product(df):
    """
    Find the year-wise most sold product.

    Args:
      df: Pandas DataFrame.

    Returns:
      A new dataframe with year, Product id of the most sold product and Units sold of that product.
    """
    df["Year"] = df["Date"].dt.year
    # Group by 'Year' and 'Product_ID' and aggregate the total units sold
    # yearly_sales = df[df['Year'] == 2023]
    yearly_sales = df.groupby(["Year", "Product_ID"])["Units_Sold"].sum()

    # Find the most sold product for each year
    df_most_sold_per_year = yearly_sales.loc[2023].idxmax()
    print(df_most_sold_per_year)
    # Display the result
    return df_most_sold_per_year


most_sold_product(df)
