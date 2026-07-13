## Rental Price Prediction - Indian Housing Dataset

Predicts monthly rent for Indian rental properties using Linear Regression, with a focus on handling extreme outliers in the target variable.

### Dataset

Source: Kaggle - Indian housing/rent dataset (4,746 listings across major
Indian cities: Mumbai, Delhi, Bangalore, Chennai, Hyderabad, Kolkata).
Features include BHK, size (sq ft), number of bathrooms, city, area type,
and furnishing status.

### Problem

Rent varies enormously across this dataset - from ₹1,200 to ₹35,00,000 - with 75% of properties renting under ₹33,000. This heavy right-skew meant a small number of luxury properties dominated the model's error during training, badly hurting prediction accuracy on typical homes.

### Approach

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

### Key Results

| Metric | Before Log Transform | After Log Transform |
| ------ | -------------------- | ------------------- |
| RMSE   | ₹43,654              | ₹30,891             |
| R²     | 0.52                 | 0.76                |

Applying the log transform reduced RMSE by ~29% and raised R² from 0.52 to
0.76, confirming that outlier-driven skew was a major source of model error.

### Key Insights

- **Location dominates rent prediction.** City coefficients were the strongest
  in the model — Mumbai showed the largest positive effect on rent (relative
  to baseline city Bangalore), while Kolkata showed the strongest negative
  effect, consistent with real-world rental market patterns in India.
- **Furnishing status matters, but less than location.** Unfurnished homes
  rent for noticeably less than furnished ones; semi-furnished falls in between.
- **Physical size has surprisingly little standalone effect.** Size (sq ft)
  had a near-zero coefficient, likely because city-level location effects
  already capture much of the price variation tied to typical property sizes
  in that market.
- **The model still struggles with high-rent outliers**, as shown in the
  actual-vs-predicted plot — predictions for luxury properties are
  inconsistent (sometimes over-, sometimes under-predicted), suggesting
  missing features (locality, floor, amenities) and non-linear pricing
  dynamics at the high end.
