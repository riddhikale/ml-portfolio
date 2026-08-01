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


@app.post("/predict", response_model=ChurnResponse)
def predict(request: ChurnRequest):
    try:
        X = pd.DataFrame([request.model_dump()])[features]
        X_scaled = scaler.transform(X)
        prob = model.predict_proba(X_scaled)[0][1]
        return {"churn_probability": round(float(prob), 4), "churn_prediction": int(prob > 0.5)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))