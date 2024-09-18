import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, HuberRegressor

# Data
ce = np.array([6.495, 6.595, 6.615, 6.635, 6.485, 6.555, 6.665, 6.505, 
               6.435, 6.625, 6.715, 6.655, 6.755, 6.625, 6.715, 6.575, 
               6.655, 6.605, 6.565, 6.515, 6.555, 6.395, 6.775, 6.685])

# Generate dummy x data (you can replace this with actual data if available)
x = np.arange(len(ce)).reshape(-1, 1)  # Create a feature array for linear regression

# 1. Traditional Linear Regression (OLS)
ols = LinearRegression()
ols.fit(x, ce)
ols_pred = ols.predict(x)

# 2. Robust Regression (Huber M-estimator)
huber = HuberRegressor()
huber.fit(x, ce)
huber_pred = huber.predict(x)

# Plot the results for comparison
plt.figure(figsize=(10, 6))
plt.scatter(x, ce, label='Data points', color='blue')
plt.plot(x, ols_pred, label='OLS (Linear Regression)', color='green', linewidth=2)
plt.plot(x, huber_pred, label='Huber M-estimator', color='red', linestyle='--', linewidth=2)
plt.xlabel('x')
plt.ylabel('ce')
plt.title('Comparison of OLS vs. Huber M-estimator')
plt.legend()
plt.grid(True)
plt.show()

# Print coefficients and intercepts for comparison
print(f"OLS Coefficients: {ols.coef_[0]:.5e}, Intercept: {ols.intercept_:.5e}")
print(f"Huber Coefficients: {huber.coef_[0]:.5e}, Intercept: {huber.intercept_:.5e}")
