# Credit Card Fraud Detection — Logistic Regression

Detects fraudulent credit card transactions using Logistic Regression, with a
focus on handling severe class imbalance (0.97% fraud) and tuning the
decision threshold to prioritize catching real fraud cases.

## Dataset

Source: ULB Machine Learning Group Credit Card Fraud dataset (Kaggle). Due to
file size, a stratified sample of 50,492 transactions is used (all 492
original fraud cases + 50,000 randomly sampled legitimate transactions),
preserving a severe imbalance (~0.97% fraud). Features V1-V28 are
PCA-transformed and anonymized for privacy; `Time` and `Amount` are the only
original, untransformed features. Target: `Class` (1 = fraud, 0 = legitimate).

Full dataset: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

## Problem

Only 0.97% of transactions in this sample are fraudulent. A model that always
predicts "not fraud" would score 99.03% accuracy without learning anything —
making accuracy nearly useless as an evaluation metric here. Precision,
recall, and F1 matter far more, and missing a fraud case (false negative)
means a direct, real financial loss.
