## Rental Price Prediction - Indian Housing Dataset

Predicts monthly rent for Indian rental properties using Linear Regression, with a focus on handling extreme outliers in the target variable.

### Dataset

Source: Kaggle — Indian housing/rent dataset (4,746 listings across major
Indian cities: Mumbai, Delhi, Bangalore, Chennai, Hyderabad, Kolkata).
Features include BHK, size (sq ft), number of bathrooms, city, area type,
and furnishing status.

### Problem

Rent varies enormously across this dataset - from ₹1,200 to ₹35,00,000 - with 75% of properties renting under ₹33,000. This heavy right-skew meant a small number of luxury properties dominated the model's error during training, badly hurting prediction accuracy on typical homes.

## Approach

1. Exploratory data analysis on rent distribution, city-wise patterns, and
   feature correlations.
2. Preprocessing: dropped irrelevant columns, checked for nulls, one-hot
   encoded categorical features (City, Area Type, Furnishing Status),
   converted boolean columns to int.
3. Identified severe right-skew in the target (Rent) — applied a `log1p`
   transform to compress the scale and reduce the influence of outliers.
4. Trained a Linear Regression model on the log-transformed target.
5. Converted predictions back to real rupees using `expm1` before evaluating,
   so metrics are interpretable in actual currency.
