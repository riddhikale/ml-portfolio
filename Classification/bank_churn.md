## Bank Customer Churn Prediction — Logistic Regression

Predicts whether a bank customer will churn (leave the bank) using Logistic
Regression, with feature scaling, threshold tuning, and controlled prediction
experiments to validate model behavior.

### Dataset

Source: Kaggle — Churn Modelling dataset, 10,000 bank customer records.
Features include CreditScore, Geography, Gender, Age, Tenure, Balance,
NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary. Target: `Exited`
(1 = churned, 0 = stayed). Identifier columns (RowNumber, CustomerId, Surname)
were dropped as they carry no predictive signal.

### Problem

Only ~20% of customers churned, making this an imbalanced classification
problem. A model that simply predicted "no churn" for everyone would already
score ~80% accuracy without learning anything useful — so accuracy alone is a
misleading metric here, and precision/recall/F1 matter far more.

### Approach

1. EDA: checked nulls, data types, and class balance.
2. Evaluated Balance = 0 for possible disguised missing values (as seen in
   the earlier Diabetes project) — but concluded this is a genuine, valid
   value (many real customers legitimately hold a zero balance), so it was
   left unchanged rather than imputed.
3. Dropped identifier columns (RowNumber, CustomerId, Surname).
4. One-hot encoded Geography and Gender.
5. Split data using stratified sampling to preserve the ~80/20 class balance.
6. Applied `StandardScaler` to features — required here because Logistic
   Regression failed to converge (ConvergenceWarning) due to wildly different
   feature scales (e.g., Balance in the hundreds of thousands vs Tenure in
   single digits).
7. Trained Logistic Regression on scaled features.
8. Evaluated using Accuracy, Precision, Recall, F1.
9. Tuned the classification threshold (0.5 → 0.3) to prioritize recall, since
   missing a customer about to churn is more costly than a false alarm.
10. Interpreted coefficients and validated them with controlled hypothetical
    predictions.

### Key Results

| Metric    | Threshold 0.5 | Threshold 0.3 |
| --------- | ------------- | ------------- |
| Accuracy  | 0.81          | 0.79          |
| Precision | 0.59          | 0.49          |
| Recall    | 0.19          | 0.52          |
| F1 Score  | 0.28          | 0.50          |

Lowering the threshold nearly tripled recall (0.19 → 0.52), a meaningful
improvement, but recall still misses roughly half of true churners — a
genuine limitation of this model (see Conclusion).

### Key Insights

- **Age** is the strongest predictor of churn — older customers are
  significantly more likely to leave.
- **IsActiveMember** has a strong negative effect — actively engaged customers
  are far less likely to churn, a directly actionable insight for retention
  strategy.
- **Geography_Germany** shows notably higher churn risk compared to the
  baseline (France).
- A controlled prediction experiment (varying only Age, IsActiveMember, and
  Geography_Germany, holding all else constant) showed predicted churn
  probability swinging from 78% (high-risk profile) to 6% (low-risk profile) —
  confirming the model's coefficients translate into consistent, sensible
  real-world behavior.

## Conclusion

Logistic Regression achieved reasonable overall accuracy but struggled with
recall, even after threshold tuning — likely because churn depends on
non-linear combinations of features (e.g., older AND inactive AND high
balance together) that a linear decision boundary can't fully capture. This
points to tree-based models (Decision Tree, Random Forest) as a natural next
step for improving churn detection.

## Next Steps

- Train a Random Forest on this same dataset for direct before/after
  comparison against Logistic Regression.
- Add an ROC-AUC curve to evaluate performance across all thresholds at once,
  rather than comparing only two fixed thresholds.
- Use cross-validation instead of a single train/test split to check model
  stability.
- Explore feature importance from tree-based models as a more powerful
  alternative to linear coefficients.

### Problem

Only ~20% of customers churned, making this an imbalanced classification
problem. A model that simply predicted "no churn" for everyone would already
score ~80% accuracy without learning anything useful — so accuracy alone is a
misleading metric here, and precision/recall/F1 matter far more.

### Approach

1. EDA: checked nulls, data types, and class balance.
2. Evaluated Balance = 0 for possible disguised missing values (as seen in
   the earlier Diabetes project) — but concluded this is a genuine, valid
   value (many real customers legitimately hold a zero balance), so it was
   left unchanged rather than imputed.
3. Dropped identifier columns (RowNumber, CustomerId, Surname).
4. One-hot encoded Geography and Gender.
5. Split data using stratified sampling to preserve the ~80/20 class balance.
6. Applied `StandardScaler` to features — required here because Logistic
   Regression failed to converge (ConvergenceWarning) due to wildly different
   feature scales (e.g., Balance in the hundreds of thousands vs Tenure in
   single digits).
7. Trained Logistic Regression on scaled features.
8. Evaluated using Accuracy, Precision, Recall, F1.
9. Tuned the classification threshold (0.5 → 0.3) to prioritize recall, since
   missing a customer about to churn is more costly than a false alarm.
10. Interpreted coefficients and validated them with controlled hypothetical
    predictions.

### Key Results

| Metric    | Threshold 0.5 | Threshold 0.3 |
| --------- | ------------- | ------------- |
| Accuracy  | 0.81          | 0.79          |
| Precision | 0.59          | 0.49          |
| Recall    | 0.19          | 0.52          |
| F1 Score  | 0.28          | 0.50          |

Lowering the threshold nearly tripled recall (0.19 → 0.52), a meaningful
improvement, but recall still misses roughly half of true churners — a
genuine limitation of this model (see Conclusion).

### Key Insights

- **Age** is the strongest predictor of churn — older customers are
  significantly more likely to leave.
- **IsActiveMember** has a strong negative effect — actively engaged customers
  are far less likely to churn, a directly actionable insight for retention
  strategy.
- **Geography_Germany** shows notably higher churn risk compared to the
  baseline (France).
- A controlled prediction experiment (varying only Age, IsActiveMember, and
  Geography_Germany, holding all else constant) showed predicted churn
  probability swinging from 78% (high-risk profile) to 6% (low-risk profile) —
  confirming the model's coefficients translate into consistent, sensible
  real-world behavior.

### Conclusion

Logistic Regression achieved reasonable overall accuracy but struggled with
recall, even after threshold tuning — likely because churn depends on
non-linear combinations of features (e.g., older AND inactive AND high
balance together) that a linear decision boundary can't fully capture. This
points to tree-based models (Decision Tree, Random Forest) as a natural next
step for improving churn detection.
