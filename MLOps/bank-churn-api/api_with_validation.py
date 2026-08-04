from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from schemas import ChurnRequest, ChurnResponse
 
app = FastAPI(title="Churn Prediction API - Real Model (Decision Tree)")

