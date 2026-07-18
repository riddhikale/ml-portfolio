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

## Approach

1. EDA: checked nulls, data types, and the severity of class imbalance.
2. Split data using stratified sampling to preserve the ~0.97% fraud ratio in
   both train and test sets.
3. Trained Logistic Regression as a baseline.
4. Evaluated using Accuracy, Precision, Recall, F1 — with extra decimal
   precision (4 decimals instead of 2), since values this close to 1.0 can
   hide meaningful differences at lower precision.
5. Tuned the classification threshold (0.5 → 0.3) to prioritize recall, given
   the high cost of missing real fraud.
6. Made a deliberate decision not to pursue a more complex model (e.g.,
   Decision Tree), given the strong baseline performance and diminishing
   returns from threshold tuning alone.

## Key Results

| Metric    | Threshold 0.5 | Threshold 0.3 |
| --------- | ------------- | ------------- |
| Accuracy  | 0.9981        | 0.9981        |
| Precision | 0.9759        | 0.9341        |
| Recall    | 0.8265        | 0.8673        |
| F1 Score  | 0.8950        | 0.8995        |

Lowering the threshold improved recall from 82.65% to 86.73%, catching more
true fraud cases at a modest precision cost. The improvement was smaller than
in earlier projects (Diabetes, Bank Churn), suggesting the model already had
strong separation between fraud and legitimate transactions before any
threshold adjustment.

## Key Insights

- **Accuracy is nearly meaningless on severely imbalanced data.** A 99%+
  accuracy score here is barely better than doing nothing at all — precision,
  recall, and F1 are the metrics that actually matter.
- **PCA-transformed features likely gave Logistic Regression a strong head
  start.** Since PCA is designed to capture the directions of maximum
  variance in the data, and fraud vs. legitimate transactions genuinely
  differ a lot, much of the separating signal was likely already present in
  V1-V28 before any modeling began — explaining why even a simple linear
  model performed well here.
- **More complex models aren't always the right call.** Given the strong
  baseline and modest gains from threshold tuning, adding a more complex
  model (like a Decision Tree) wasn't clearly justified for this dataset — a
  deliberate, defensible modeling decision rather than a shortcut.
