"""Generate a reproducible synthetic retail sales dataset."""
from pathlib import Path
import numpy as np
import pandas as pd

def generate_sales(n=600, seed=42):
    rng = np.random.default_rng(seed)
    products = ["Laptop Stand", "Wireless Mouse", "Keyboard", "USB Hub", "Monitor", "Webcam"]
    price_map = {"Laptop Stand": 25.0, "Wireless Mouse": 18.0, "Keyboard": 45.0,
                 "USB Hub": 22.0, "Monitor": 180.0, "Webcam": 65.0}
    category_map = {p: ("Electronics" if p in ["Monitor", "Webcam"] else "Accessories") for p in products}
    dates = pd.Timestamp("2025-01-01") + pd.to_timedelta(rng.integers(0, 304, n), unit="D")
    product = rng.choice(products, n)
    df = pd.DataFrame({
        "Order_ID": [f"ORD{i+1:04d}" for i in range(n)],
        "Order_Date": dates,
        "Customer_ID": [f"CUST{x:03d}" for x in rng.integers(1, 121, n)],
        "Product": product,
        "Category": [category_map[p] for p in product],
        "Region": rng.choice(["South", "North", "East", "West"], n),
        "Quantity": rng.integers(1, 6, n),
        "Unit_Price": [round(price_map[p] * float(rng.uniform(.9, 1.12)), 2) for p in product],
        "Discount": rng.choice([0, .05, .10, .15], n),
        "Payment_Method": rng.choice(["Card", "UPI", "Cash", "Net Banking"], n),
    })
    return df

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    out = root / "data" / "raw" / "sales.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    generate_sales().to_csv(out, index=False)
    print(f"Wrote {out}")
