from fastapi import FastAPI
import joblib
import pandas as pd
 
app = FastAPI(title="Churn Prediction API - v1 (no validation yet)")