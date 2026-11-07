"""Reusable summaries using NumPy and Pandas only."""
import numpy as np
import pandas as pd

def create_summaries(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    revenue_by_product = (
        df.groupby("Product", as_index=False)
          .agg(Units_Sold=("Quantity", "sum"),
               Orders=("Order_ID", "nunique"),
               Revenue=("Net_Sales", "sum"),
               Average_Unit_Price=("Unit_Price", "mean"))
          .sort_values("Revenue", ascending=False)
    )
    revenue_by_region = (
        df.groupby("Region", as_index=False)
          .agg(Orders=("Order_ID", "nunique"),
               Customers=("Customer_ID", "nunique"),
               Revenue=("Net_Sales", "sum"))
          .sort_values("Revenue", ascending=False)
    )
    monthly = (
        df.groupby("Month", as_index=False)
          .agg(Orders=("Order_ID", "nunique"), Revenue=("Net_Sales", "sum"))
          .sort_values("Month")
    )
    customer = (
        df.groupby("Customer_ID", as_index=False)
          .agg(Orders=("Order_ID", "nunique"),
               Revenue=("Net_Sales", "sum"),
               Average_Order_Value=("Net_Sales", "mean"))
          .sort_values("Revenue", ascending=False)
    )
    values = df["Net_Sales"].to_numpy(dtype=float)
    q1, q3 = np.percentile(values, [25, 75])
    iqr = q3 - q1
    outlier_mask = (values < q1 - 1.5 * iqr) | (values > q3 + 1.5 * iqr)
    outliers = df.loc[outlier_mask].copy()
    outliers["Outlier_Reason"] = "Net_Sales outside 1.5*IQR fences"
    return {
        "revenue_by_product": revenue_by_product,
        "revenue_by_region": revenue_by_region,
        "monthly_revenue": monthly,
        "customer_summary": customer,
        "potential_outliers": outliers,
    }
