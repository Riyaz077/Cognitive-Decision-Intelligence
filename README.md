# Cognitive Decision Intelligence Framework for Dynamic Business Strategy Using AI

An end-to-end AI-powered decision intelligence system integrating **Machine Learning, Predictive Analytics, Natural Language Processing, and Business Intelligence** to analyse multiple business domains, compare predictive models, generate actionable insights, and support data-driven strategic decision-making.

The project evaluates machine-learning models across three datasets: Walmart Retail Sales, Amazon Customer Reviews, and M5 Retail Forecasting, with an interactive **Streamlit dashboard** for performance analysis and visualization.

## Project Overview

The framework combines predictive modelling, analytical evaluation, and business intelligence to transform raw business data into meaningful insights.

It focuses on three major analytical domains:

| Dataset | Business Problem | Machine Learning Models |
|---|---|---|
| Walmart | Weekly retail sales forecasting | Linear Regression, Random Forest, XGBoost |
| Amazon Reviews | Customer sentiment classification | Logistic Regression, Multinomial Naive Bayes, Linear SVM |
| M5 | Large-scale retail demand forecasting | XGBoost, LightGBM, LSTM |

## Project Objectives

- Develop predictive models across multiple business domains.
- Analyse retail sales, customer sentiment, and demand patterns.
- Compare machine-learning algorithms using appropriate evaluation metrics.
- Identify high-performing models for each analytical task.
- Generate meaningful insights through predictive and comparative analytics.
- Develop an interactive dashboard for intelligent business decision-making.

## System Architecture

```text
              Business Datasets
                     |
        +------------+------------+
        |            |            |
     Walmart       Amazon         M5
        |            |            |
   Preprocessing  Text Cleaning  Preprocessing
        |            |            |
   Sales Models  Sentiment Models Forecasting Models
        |            |            |
        +------------+------------+
                     |
             Model Evaluation
                     |
          Comparative Analytics
                     |
          Unified Results Dataset
                     |
           Business Intelligence
                     |
          Streamlit Dashboard
                     |
          Decision Intelligence
```

## Methodology

1. **Data Collection** – Load Walmart, Amazon Reviews, and M5 datasets.
2. **Data Preprocessing** – Handle missing values, clean data, and prepare features.
3. **Exploratory Data Analysis** – Identify patterns, distributions, and relationships.
4. **Feature Engineering** – Generate relevant features for predictive modelling.
5. **Model Development** – Implement multiple machine-learning algorithms for each dataset.
6. **Model Evaluation** – Evaluate performance using appropriate metrics.
7. **Comparative Analysis** – Compare models and identify their relative performance.
8. **Business Insights** – Translate analytical findings into meaningful recommendations.
9. **Dashboard Development** – Integrate analytical outputs into an interactive Streamlit application.

## Technology Stack

**Programming Languages**
- Python

**Data Science & Machine Learning**
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM

**Deep Learning & NLP**
- TensorFlow / Keras
- Natural Language Processing
- LSTM
- TF-IDF

**Visualization & Business Intelligence**
- Matplotlib
- Seaborn
- Plotly
- Streamlit

**Development Environment**
- Jupyter Notebook
- Google Colab
- Visual Studio Code
- Git & GitHub

## Results & Analytics

The framework provides:

- Comparative evaluation of machine-learning models across three business domains.
- Predictive performance analysis for retail sales, sentiment classification, and demand forecasting.
- Dataset-wise model comparisons using appropriate evaluation metrics.
- Visual exploration of model performance and analytical patterns.
- Consolidated evaluation results through `unified_model_results.csv`.
- Interactive analytical dashboards for exploring model outputs.
- Business insights to support informed and data-driven strategic decisions.

*Actual performance metrics and model rankings should be reported using measured experimental results.*

## Interactive Dashboard

The Streamlit application provides an integrated interface for exploring analytical results, comparing predictive models, visualizing performance metrics, and generating business-oriented insights.

## Responsible Reporting

- Evaluate models using appropriate held-out test datasets.
- Apply chronological train-test splits for time-series forecasting.
- Avoid data leakage during preprocessing and model training.
- Report actual experimental results without fabricating performance scores.
- Respect dataset licensing and privacy requirements.

## Repository Structure

```text
├── app.py
├── requirements.txt
├── README.md
├── data/
├── notebooks/
├── models/
├── results/
├── screenshots/
├── presentation/
├── src/
│   ├── data_preprocessing/
│   ├── models/
│   └── analytics/
├── docs/
└── tests/
```

## Getting Started

**1. Clone the repository**

```bash
git clone <your-repository-url>
cd <repository-folder>
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Prepare the datasets**

Place the Walmart, Amazon Reviews, and M5 datasets in their respective directories under `data/`.

**5. Run the Streamlit dashboard**

```bash
streamlit run app.py
```

**6. Run project tests**

```bash
pytest -q
```

*Ensure that the dataset paths, dependencies, and scripts match the actual repository implementation.*

## Author

**Mohamed Riyaz S.**  
Integrated M.Tech – Computer Science and Engineering (Business Analytics)  
Vellore Institute of Technology (VIT), Chennai
