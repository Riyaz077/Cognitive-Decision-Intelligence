"""Baseline model factories and reproducible training helpers."""
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

def amazon_models(max_features=5000):
    return {
        "Logistic Regression": Pipeline([
            ("tfidf", TfidfVectorizer(max_features=max_features, stop_words="english")),
            ("model", LogisticRegression(max_iter=1000, class_weight="balanced"))
        ]),
        "Naive Bayes": Pipeline([
            ("tfidf", TfidfVectorizer(max_features=max_features, stop_words="english")),
            ("model", MultinomialNB())
        ]),
        "Linear SVM": Pipeline([
            ("tfidf", TfidfVectorizer(max_features=max_features, stop_words="english")),
            ("model", LinearSVC(class_weight="balanced"))
        ])
    }

def walmart_baselines(random_state=42):
    return {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(
            n_estimators=200, random_state=random_state, n_jobs=-1
        )
    }

def optional_xgboost_regressor(random_state=42):
    from xgboost import XGBRegressor
    return XGBRegressor(
        n_estimators=300, max_depth=6, learning_rate=0.05,
        subsample=0.8, colsample_bytree=0.8,
        objective="reg:squarederror", random_state=random_state, n_jobs=-1
    )
