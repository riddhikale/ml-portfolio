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
