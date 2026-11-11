"""Walmart dataset loading and basic feature preparation."""
from pathlib import Path
import pandas as pd

def load_walmart(data_dir="data/walmart"):
    path = Path(data_dir)
    required = ["train.csv", "features.csv", "stores.csv"]
    missing = [f for f in required if not (path / f).exists()]
    if missing:
        raise FileNotFoundError(f"Missing Walmart files in {path}: {missing}")
    train = pd.read_csv(path / "train.csv")
    features = pd.read_csv(path / "features.csv")
    stores = pd.read_csv(path / "stores.csv")
    return train, features, stores

def prepare_walmart(data_dir="data/walmart"):
    train, features, stores = load_walmart(data_dir)
    df = train.merge(features, on=["Store", "Date", "IsHoliday"], how="left")
    df = df.merge(stores, on="Store", how="left")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date", "Weekly_Sales"])
    for col in [c for c in df.columns if c.startswith("MarkDown")]:
        df[col] = df[col].fillna(0)
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Week"] = df["Date"].dt.isocalendar().week.astype(int)
    df["IsHoliday"] = df["IsHoliday"].astype(int)
    for col in ["Type"]:
        if col in df:
            df[col] = df[col].astype("category").cat.codes
    df = df.sort_values(["Store", "Dept", "Date"])
    return df
