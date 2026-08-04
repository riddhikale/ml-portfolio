"""
Trains the churn model on the REAL bank_churn.csv dataset, using the exact preprocessing from Logistic_Regression_Decision_Tree_Bank_Churn.ipynb.
 
Both Logistic Regression and Decision Tree were tested on this data.
Decision Tree wins clearly on recall/F1 (0.40/0.53 vs 0.19/0.28), which matters more for churn - missing an actual churner is costlier than a false alarm.
So Decision Tree is the one deployed here.
"""

import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score