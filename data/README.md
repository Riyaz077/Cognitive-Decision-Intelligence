# Dataset setup

Do not commit raw datasets unless their licenses explicitly permit redistribution and the files are within GitHub limits.

Expected layout:

```text
data/
├── walmart/
│   ├── train.csv
│   ├── test.csv
│   ├── features.csv
│   └── stores.csv
├── amazon_reviews/
│   └── reviews.csv
└── m5/
    ├── calendar.csv
    ├── sales_train_validation.csv
    ├── sales_train_evaluation.csv
    └── sell_prices.csv
```

The Amazon review data should contain a rating column (`Score` or `overall`) and a text column (`Text` or `reviewText`). Verify column names and label definitions against your exact source release.

Download datasets from their original authorized sources and preserve their attribution and terms. This repository does not bundle the datasets.
