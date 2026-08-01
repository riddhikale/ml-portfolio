import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import joblib
import os


np.random.seed(42)

n = 2000
age = np.random.randint(18, 75, n)
tenure = np.random.randint(0, 15, n)
balance = np.random.exponential(scale=50000, size=n)
num_products = np.random.randint(1, 4, n)
is_active = np.random.binomial(1, 0.6, n)


churn_logit = (
    -0.03 * age
    - 0.15 * tenure
    + 0.00002 * balance
    - 0.4 * num_products
    - 1.2 * is_active
    + np.random.normal(0, 1, n)
)

churn_prob = 1 / (1 + np.exp(-churn_logit))
churned = (churn_prob > np.median(churn_prob)).astype(int)


df = pd.DataFrame({
    "age": age,
    "tenure": tenure,
    "balance": balance,
    "num_products": num_products,
    "is_active": is_active,
    "churned": churned,
})


FEATURES = ["age", "tenure", "balance", "num_products", "is_active"]
X = df[FEATURES]
y = df["churned"]
 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
 
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
 
y_pred = model.predict(X_test_scaled)
print(classification_report(y_test, y_pred))