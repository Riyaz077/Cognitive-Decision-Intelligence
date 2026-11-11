"""M5 wide-to-long conversion and leakage-aware lag feature helper."""
from pathlib import Path
import pandas as pd

def load_m5(data_dir="data/m5", sales_file="sales_train_validation.csv"):
    path = Path(data_dir)
    needed = [sales_file, "calendar.csv", "sell_prices.csv"]
    missing = [f for f in needed if not (path / f).exists()]
    if missing:
        raise FileNotFoundError(f"Missing M5 files in {path}: {missing}")
    sales = pd.read_csv(path / sales_file)
    calendar = pd.read_csv(path / "calendar.csv")
    prices = pd.read_csv(path / "sell_prices.csv")
    return sales, calendar, prices

def to_long_m5(sales, calendar, prices, sample_items=None):
    id_cols = ["id", "item_id", "dept_id", "cat_id", "store_id", "state_id"]
    id_cols = [c for c in id_cols if c in sales.columns]
    day_cols = [c for c in sales.columns if c.startswith("d_")]
    if not day_cols:
        raise ValueError("No d_1, d_2, ... sales columns found.")
    if sample_items:
        keep = sales["id"].drop_duplicates().head(sample_items)
        sales = sales[sales["id"].isin(keep)]
    long_df = sales.melt(id_vars=id_cols, value_vars=day_cols,
                         var_name="d", value_name="sales")
    long_df = long_df.merge(calendar, on="d", how="left")
    join_keys = [c for c in ["store_id", "item_id", "wm_yr_wk"] if c in long_df and c in prices]
    if len(join_keys) == 3:
        long_df = long_df.merge(prices, on=join_keys, how="left")
    long_df["sales"] = pd.to_numeric(long_df["sales"], errors="coerce")
    long_df = long_df.sort_values(["id", "date"] if "date" in long_df else ["id", "d"])
    return long_df

def add_lag_features(df, group_col="id", target="sales", lags=(7, 28)):
    out = df.copy()
    out = out.sort_values([group_col, "date"] if "date" in out else [group_col, "d"])
    for lag in lags:
        out[f"lag_{lag}"] = out.groupby(group_col)[target].shift(lag)
    return out
