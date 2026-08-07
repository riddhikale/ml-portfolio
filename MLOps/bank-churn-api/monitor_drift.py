import json
import pandas as pd
 
 
def load_logged_inputs(log_path="logs/predictions.log"):
    rows = []
    with open(log_path) as f:
        for line in f:
            entry = json.loads(line)
            rows.append(entry["input"])
    return pd.DataFrame(rows)


def load_training_data(csv_path="bank_churn.csv"):
    df = pd.read_csv(csv_path)
    # rename to match the API's request field names for a fair comparison
    df = df.rename(columns={
        "CreditScore": "credit_score",
        "Age": "age",
        "Tenure": "tenure",
        "Balance": "balance",
        "NumOfProducts": "num_of_products",
        "EstimatedSalary": "estimated_salary",
    })
    return df
 
 
def compare_distributions(logged_df, training_df, numeric_cols):
    print(f"{'Feature':<20}{'Training Mean':>15}{'Logged Mean':>15}{'% Shift':>12}")
    print("-" * 62)
    for col in numeric_cols:
        train_mean = training_df[col].mean()
        logged_mean = logged_df[col].mean()
        pct_shift = abs(logged_mean - train_mean) / train_mean * 100 if train_mean != 0 else 0
        flag = "  <-- CHECK THIS" if pct_shift > 20 else ""
        print(f"{col:<20}{train_mean:>15.2f}{logged_mean:>15.2f}{pct_shift:>11.1f}%{flag}")


def load_training_data(csv_path="bank_churn.csv"):
    df = pd.read_csv(csv_path)
    # rename to match the API's request field names for a fair comparison
    df = df.rename(columns={
        "CreditScore": "credit_score",
        "Age": "age",
        "Tenure": "tenure",
        "Balance": "balance",
        "NumOfProducts": "num_of_products",
        "EstimatedSalary": "estimated_salary",
    })
    return df
 
 
def compare_distributions(logged_df, training_df, numeric_cols):
    print(f"{'Feature':<20}{'Training Mean':>15}{'Logged Mean':>15}{'% Shift':>12}")
    print("-" * 62)
    for col in numeric_cols:
        train_mean = training_df[col].mean()
        logged_mean = logged_df[col].mean()
        pct_shift = abs(logged_mean - train_mean) / train_mean * 100 if train_mean != 0 else 0
        flag = "  <-- CHECK THIS" if pct_shift > 20 else ""
        print(f"{col:<20}{train_mean:>15.2f}{logged_mean:>15.2f}{pct_shift:>11.1f}%{flag}")
 