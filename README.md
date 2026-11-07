# NumPy + Pandas Sales Analysis Toolkit

A hands-on Data Science portfolio project built using **Python, NumPy, and Pandas only** for analysis and data processing. The dataset is synthetic and intentionally contains data-quality issues for practice.

## Goals
- Practise NumPy arrays, vectorized operations, statistics, random sampling, percentiles, and outlier detection.
- Practise Pandas loading, inspection, cleaning, filtering, grouping, merging, reshaping, datetime operations, and exporting.
- Produce reproducible analysis outputs and a concise findings report.
- Build a GitHub portfolio project without machine learning or visualization libraries.

## Dataset
`data/raw/sales.csv` contains synthetic retail transactions with columns:
- `Order_ID`, `Order_Date`, `Customer_ID`, `Product`, `Category`, `Region`
- `Quantity`, `Unit_Price`, `Discount`, `Payment_Method`

The raw file deliberately includes missing values, inconsistent region formatting, and duplicate rows. Keep it unchanged and write cleaned output to `data/processed/`.

## Setup
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
jupyter notebook
```

## Suggested learning sequence
1. `notebooks/01_numpy_fundamentals.ipynb`
2. `notebooks/02_pandas_fundamentals.ipynb`
3. `notebooks/03_data_cleaning.ipynb`
4. `notebooks/04_sales_eda.ipynb`
5. `notebooks/05_advanced_analysis.ipynb`

## Run the pipeline
```bash
python src/main.py
```

## Outputs
The pipeline writes cleaned transactions and summary CSV files to `data/processed/` and a Markdown summary to `reports/findings.md`.

## Methods practised
NumPy: `array`, `where`, `mean`, `median`, `std`, `percentile`, `quantile`, `sum`, `unique`, `bincount`, `select`, `clip`, `random.default_rng`, `isfinite`.

Pandas: `read_csv`, `to_csv`, `head`, `info`, `describe`, `isna`, `duplicated`, `drop_duplicates`, `to_numeric`, `to_datetime`, `fillna`, `groupby`, `agg`, `sort_values`, `merge`, `pivot_table`, `melt`, `resample`, `rolling`, `nunique`, `value_counts`, `assign`, `query`.

## Important
This is an educational synthetic dataset, not real customer or business data. Outlier flags indicate unusual observations, not necessarily errors.
