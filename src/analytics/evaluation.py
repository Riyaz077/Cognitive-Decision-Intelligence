"""Common evaluation helpers and result-table persistence."""
from pathlib import Path
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score, precision_recall_fscore_support

def regression_metrics(y_true, y_pred):
    return {
        "MAE": float(mean_absolute_error(y_true, y_pred)),
        "RMSE": float(mean_squared_error(y_true, y_pred) ** 0.5),
        "R2": float(r2_score(y_true, y_pred))
    }

def classification_metrics(y_true, y_pred):
    p, r, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average="binary", zero_division=0
    )
    return {"Accuracy": float(accuracy_score(y_true, y_pred)),
            "Precision": float(p), "Recall": float(r), "F1": float(f1)}

def save_metrics(records, output="results/unified_model_results.csv"):
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(records)
    expected = {"Dataset", "Model", "Metric", "Value"}
    if not expected.issubset(df.columns):
        raise ValueError(f"Records must include columns: {sorted(expected)}")
    df.to_csv(path, index=False)
    return df
