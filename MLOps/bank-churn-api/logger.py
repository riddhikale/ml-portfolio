from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from schemas import ChurnRequest, ChurnResponse
from logger import log_prediction
 
app = FastAPI(title="Churn Prediction API - Real Model (Decision Tree)")