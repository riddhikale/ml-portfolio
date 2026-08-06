from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from schemas import ChurnRequest, ChurnResponse
from logger import log_prediction

app = FastAPI(title="Churn Prediction API - Real Model (Decision Tree)")

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
        row = request.to_model_input()
        X = pd.DataFrame([row])[features]  
        X_scaled = scaler.transform(X)
        prob = model.predict_proba(X_scaled)[0][1]
        result = {"churn_probability": round(float(prob), 4), "churn_prediction": int(prob > 0.5)}

        log_prediction(input_data=request.model_dump(), output_data=result)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))