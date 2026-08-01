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


@app.post("/predict")
def predict(payload: dict):
    # payload is a raw dict here - if a key is missing or wrong type,
    # this will throw an unhandled error. That's the gap #4 (validation) fixes.
    X = pd.DataFrame([payload])[features]
    X_scaled = scaler.transform(X)
    prob = model.predict_proba(X_scaled)[0][1]
    return {"churn_probability": round(float(prob), 4), "churn_prediction": int(prob > 0.5)}

