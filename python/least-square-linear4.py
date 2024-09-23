import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def linear_func(x, a, b):
    return a * x + b


# Provided data
x_data = np.array([10, 20, 30, 40, 50, 60, 70, 80])
y_data = np.array([25, 70, 380, 550, 610, 1220, 830, 1450])

# Fit the data using scipy's curve_fit to get the optimal slope and intercept
popt, pcov = curve_fit(linear_func, x_data, y_data)

# Extract the optimal parameters (slope and intercept)
slope, intercept = popt

# Compute the standard deviation of the parameters (errors on slope and intercept)
slope_error, intercept_error = np.sqrt(np.diag(pcov))

# Generate y values based on the fitted line
y_fit = linear_func(x_data, slope, intercept)

# Compute residuals (difference between observed and fitted values)
residuals = y_data - y_fit

# Calculate the standard deviation of the residuals to approximate the error in the data
y_errors = np.std(residuals) * np.ones_like(y_data)

# Plotting the data with computed error bars
plt.errorbar(x_data, y_data, yerr=y_errors, fmt='o',
             label='Data with error bars', capsize=5)
plt.plot(x_data, y_fit,
         label=f'Fitted line: y = {slope:.4f}x + {intercept:.4f}', color='green')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression with Computed Error Bars')
plt.legend()

# Show plot
plt.savefig('least-square-linear4.png')
plt.show()

# Print the fitted parameters with errors
print(f"Fitted slope: {slope:.2f} ± {slope_error:.2f}")
print(f"Fitted intercept: {intercept:.4f} ± {intercept_error:.4f}")
print(
    f"Residual standard deviation (error bar value): {np.std(residuals):.2f}")
