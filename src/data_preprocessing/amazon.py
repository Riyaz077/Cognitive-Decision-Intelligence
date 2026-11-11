"""Amazon review sentiment preparation."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_amazon(file_path="data/amazon_reviews/reviews.csv", max_rows=None):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Amazon review file not found: {path}")
    df = pd.read_csv(path)
    rating_col = next((c for c in ["Score", "overall"] if c in df.columns), None)
    text_col = next((c for c in ["Text", "reviewText"] if c in df.columns), None)
    if not rating_col or not text_col:
        raise ValueError("Expected rating column Score/overall and text column Text/reviewText.")
    df = df[[rating_col, text_col]].dropna()
    if max_rows:
        df = df.sample(min(max_rows, len(df)), random_state=42)
    df = df[df[rating_col] != 3].copy()
    df["sentiment"] = (df[rating_col] >= 4).astype(int)
    df[text_col] = df[text_col].astype(str)
    return df, text_col

def split_reviews(df, text_col, test_size=0.2):
    return train_test_split(
        df[text_col], df["sentiment"], test_size=test_size,
        random_state=42, stratify=df["sentiment"]
    )
