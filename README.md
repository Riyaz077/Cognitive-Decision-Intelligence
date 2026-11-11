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

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Cognitive-Decision-Intelligence.git
cd Cognitive-Decision-Intelligence
```

### 2. Create an environment

```bash
python -m venv .venv
# Windows PowerShell
.venv\\Scripts\\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add datasets

Place the original files in the directories described in [`data/README.md`](data/README.md). Dataset files are intentionally not committed because of size and licensing considerations.

### 5. Run the dashboard

```bash
streamlit run app.py
```

### 6. Run tests

```bash
pytest -q
```

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

