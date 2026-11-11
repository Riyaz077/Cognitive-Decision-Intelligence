from src.analytics.evaluation import regression_metrics, classification_metrics

def test_regression_metrics():
    result = regression_metrics([1, 2, 3], [1, 2, 3])
    assert result["MAE"] == 0
    assert result["RMSE"] == 0

def test_classification_metrics():
    result = classification_metrics([0, 1, 1], [0, 1, 0])
    assert 0 <= result["Accuracy"] <= 1
    assert "F1" in result
