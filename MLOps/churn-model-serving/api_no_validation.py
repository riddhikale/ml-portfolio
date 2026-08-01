from fastapi import FastAPI
import joblib
import pandas as pd
 
app = FastAPI(title="Churn Prediction API - v1 (no validation yet)")


artifact = joblib.load("model/churn_model.joblib")
model = artifact["model"]
scaler = artifact["scaler"]
features = artifact["features"]
 
 
@app.get("/health")
def health_check():
    return {"status": "ok"}