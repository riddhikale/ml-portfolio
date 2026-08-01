from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from schemas import ChurnRequest, ChurnResponse
 
app = FastAPI(title="Churn Prediction API - v2 (with validation)")

artifact = joblib.load("model/churn_model.joblib")
model = artifact["model"]
scaler = artifact["scaler"]
features = artifact["features"]
 
 
@app.get("/health")
def health_check():
    return {"status": "ok"}