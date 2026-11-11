# Project notebooks

Upload these notebooks to the GitHub repository's `notebooks/` folder.

## Execution order
1. `01_Walmart_Analysis.ipynb`
2. `02_Amazon_Sentiment_Analysis.ipynb`
3. `03_M5_Forecasting.ipynb`
4. `04_Model_Comparison.ipynb`

Run them from the repository root so relative paths such as `data/walmart/` and `results/` resolve correctly. Add the original authorized datasets locally; they are not included in this package. Run notebooks 01–03 before notebook 04.

Install dependencies from the repository root:
`pip install -r requirements.txt`

The M5 notebook requires `xgboost`. Notebooks write measured results to `results/`. They do not include fabricated model scores.
