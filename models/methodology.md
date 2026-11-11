# Methodology

## 1. Walmart retail sales
1. Load weekly sales, store metadata, and calendar/markdown features.
2. Merge on the dataset's documented keys.
3. Parse dates; derive year, month, week, and holiday features.
4. Handle missing markdown values and encode categorical columns.
5. Optionally derive lag and rolling features using past observations only.
6. Train Linear Regression, Random Forest, and XGBoost.
7. Evaluate on a chronological or otherwise leakage-safe holdout using MAE and RMSE; report R² where appropriate.

## 2. Amazon review sentiment
1. Load review text and star rating.
2. Remove neutral 3-star reviews if reproducing a binary positive/negative experiment.
3. Map ratings 4–5 to positive and 1–2 to negative.
4. Clean missing text and split train/test with stratification.
5. Fit TF-IDF (maximum 5,000 features) inside a scikit-learn Pipeline.
6. Compare Logistic Regression, Multinomial Naive Bayes, and Linear SVM.
7. Report accuracy, precision, recall, F1, and confusion matrix.

## 3. M5 demand forecasting
1. Read the wide sales table and melt item/store series into long format.
2. Join calendar and sell-price data using documented keys.
3. Create time and lag features (e.g. lag 7 and lag 28) using past values only.
4. For an initial experiment, sample a manageable subset of item/store series.
5. Compare XGBoost and LightGBM; LSTM is an optional sequence-model experiment.
6. Use a chronological validation split and report MAE/RMSE. Explain sampling and forecast horizon.

## 4. Decision intelligence layer
Aggregate measured evaluation metrics into a common results table. Compare models within each dataset and metric; translate findings into cautious operational implications. Avoid comparing unlike metrics (e.g. classification accuracy against forecasting RMSE) as if they were interchangeable.
