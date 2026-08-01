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