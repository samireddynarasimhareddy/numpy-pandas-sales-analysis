"""Run the NumPy + Pandas sales analysis pipeline."""
from pathlib import Path
import pandas as pd
from cleaning import clean_sales
from analysis import create_summaries

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "sales.csv"
OUT = ROOT / "data" / "processed"
REPORT = ROOT / "reports" / "findings.md"

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    raw = pd.read_csv(RAW)
    cleaned = clean_sales(raw)
    cleaned.to_csv(OUT / "sales_cleaned.csv", index=False)

    summaries = create_summaries(cleaned)
    for name, table in summaries.items():
        table.to_csv(OUT / f"{name}.csv", index=False)

    report = [
        "# Sales Analysis Findings",
        "",
        "> Generated from a synthetic educational dataset.",
        "",
        f"- Raw rows: {len(raw):,}",
        f"- Cleaned rows: {len(cleaned):,}",
        f"- Duplicate rows removed: {int(raw.duplicated().sum()):,}",
        f"- Total net sales: {cleaned['Net_Sales'].sum():,.2f}",
        f"- Unique customers: {cleaned['Customer_ID'].nunique():,}",
        f"- Unique products: {cleaned['Product'].nunique():,}",
        "",
        "## Top products by net sales",
        "",
        summaries["revenue_by_product"].head(5).to_string(index=False),
        "",
        "## Revenue by region",
        "",
        summaries["revenue_by_region"].to_string(index=False),
        "",
        "## Monthly revenue",
        "",
        summaries["monthly_revenue"].to_string(index=False),
        "",
        "## Notes",
        "",
        "- Outlier flags are prompts for investigation, not automatic evidence of bad data.",
        "- The missing-value rules are educational examples; production rules should be justified.",
    ]
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Done. Cleaned rows: {len(cleaned)}")
    print(f"Outputs: {OUT}")
    print(f"Report: {REPORT}")

if __name__ == "__main__":
    main()
