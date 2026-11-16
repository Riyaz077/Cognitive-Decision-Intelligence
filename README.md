# Cognitive Decision Intelligence Framework for Dynamic Business Strategy Using AI

An end-to-end, multi-domain predictive analytics project that evaluates machine-learning models across retail sales, customer sentiment, and large-scale retail forecasting datasets, then presents results through an interactive Streamlit dashboard.

> **Project status:** Portfolio-ready starter repository. Add your original datasets, run the pipelines, and replace illustrative/empty result areas with your measured outputs. No performance scores are fabricated in this repository.

## Business problems

| Dataset | Business problem | Models |
|---|---|---|
| Walmart | Forecast weekly store-department sales | Linear Regression, Random Forest, XGBoost |
| Amazon Reviews | Classify customer review sentiment | Logistic Regression, Multinomial Naive Bayes, Linear SVM |
| M5 | Forecast item-level retail demand | XGBoost, LightGBM, LSTM (optional TensorFlow) |

## Architecture

```text
Raw datasets
   ├── Walmart ── preprocessing ── regression models ──┐
   ├── Amazon  ── text cleaning ─── sentiment models ──┼── Unified evaluation
   └── M5      ── time features ─── forecasting models ┘
                                                           │
                                      CSV results + business insights
                                                           │
                                                Streamlit dashboard
```

## Repository structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── config/
│   └── settings.yaml
├── data/
│   └── README.md
├── docs/
│   ├── methodology.md
│   └── architecture.md
├── notebooks/
│   └── README.md
├── presentation/
│   └── project_presentation.pptx
├── results/
│   └── README.md
├── models/
│   └── README.md
├── screenshots/
│   └── README.md
├── src/
│   ├── data_preprocessing/
│   │   ├── walmart.py
│   │   ├── amazon.py
│   │   └── m5.py
│   ├── models/
│   │   └── train.py
│   └── analytics/
│       └── evaluation.py
└── tests/
    └── test_smoke.py
```

## **Quick Start**

- Clone the repository and navigate to the project directory.
- Set up and activate a Python virtual environment.
- Install all required dependencies using `requirements.txt`.
- Download and place the Walmart, Amazon Reviews, and M5 datasets in their respective data folders.
- Configure dataset paths and project settings.
- Execute the preprocessing and model-training pipelines.
- Generate and save model evaluation metrics in the `results/` directory.
- Launch the interactive Streamlit dashboard using `streamlit run app.py`.
- Run `pytest -q` to verify the project functionality.

## Expected input data

- **Walmart:** `data/walmart/train.csv`, `features.csv`, `stores.csv`
- **Amazon:** `data/amazon_reviews/reviews.csv` with review text and rating columns
- **M5:** `data/m5/sales_train_validation.csv`, `calendar.csv`, `sell_prices.csv`

Column names vary between dataset releases. The preprocessing functions validate expected columns and provide clear errors. Review the source data dictionary before training.

## Results

Place generated model metrics in `results/unified_model_results.csv`. The dashboard accepts a tidy CSV with these columns:

```csv
Dataset,Model,Metric,Value
Walmart,Random Forest,MAE,0.0
Amazon Reviews,Linear SVM,Accuracy,0.0
M5,XGBoost,RMSE,0.0
```

The values above are schema examples only. Replace `0.0` with measured results from your own runs.

## Responsible reporting

- Do not claim a model is best without comparing it on a held-out test set.
- For time series, split chronologically; do not randomly mix future observations into training.
- Report dataset sampling, hardware, runtime, feature definitions, and evaluation metrics.
- Do not upload restricted datasets, API keys, credentials, private paths, or personal information.

## Technology stack

Python · Pandas · NumPy · Scikit-learn · XGBoost · LightGBM · TensorFlow/Keras · Streamlit · Matplotlib · Plotly

## Author

**Mohamed Riyaz S.**  
Integrated M.Tech, Computer Science and Engineering (Business Analytics)  
VIT Chennai

