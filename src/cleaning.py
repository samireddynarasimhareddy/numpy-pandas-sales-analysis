"""Data quality checks and cleaning helpers using Pandas and NumPy only."""
import numpy as np
import pandas as pd

NUMERIC_COLUMNS = ["Quantity", "Unit_Price", "Discount"]

def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy; preserve the raw source file unchanged."""
    df = df.copy()
    df.columns = df.columns.str.strip()
    df = df.drop_duplicates()
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
    for col in NUMERIC_COLUMNS:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    for col in ["Product", "Category", "Region", "Payment_Method", "Customer_ID"]:
        df[col] = df[col].astype("string").str.strip()
    df["Region"] = df["Region"].str.title()
    df["Product"] = df["Product"].str.title()
    df["Category"] = df["Category"].str.title()
    df["Payment_Method"] = df["Payment_Method"].str.title()
    # Median imputation is an educational choice; inspect missingness first in real projects.
    df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
    df["Unit_Price"] = df["Unit_Price"].fillna(df.groupby("Product")["Unit_Price"].transform("median"))
    df["Discount"] = df["Discount"].fillna(0)
    df["Region"] = df["Region"].fillna("Unknown")
    df = df.dropna(subset=["Order_ID", "Order_Date", "Product", "Customer_ID"])
    df["Quantity"] = df["Quantity"].round().astype("int64")
    df["Discount"] = df["Discount"].clip(0, 1)
    df["Gross_Sales"] = df["Quantity"] * df["Unit_Price"]
    df["Net_Sales"] = df["Gross_Sales"] * (1 - df["Discount"])
    df["Year"] = df["Order_Date"].dt.year
    df["Month"] = df["Order_Date"].dt.to_period("M").astype("string")
    return df
