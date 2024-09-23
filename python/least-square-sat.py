import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def saturation_growth_rate(x, a, b):
    return (a * x) / (b + x)


# Example synthetic data (replace this with your own data)
np.random.seed(0)  # For reproducibility
x_data = np.linspace(0.1, 10, 50)
y_data = saturation_growth_rate(
    x_data, 5, 2) + np.random.normal(scale=0.5, size=x_data.size)

# Perform curve fitting using SciPy's curve_fit function
p_opt, p_cov = curve_fit(saturation_growth_rate, x_data, y_data, p0=[1, 1])

# Extract the optimal parameters
a_opt, b_opt = p_opt

# Generate y values using the fitted model
y_fit = saturation_growth_rate(x_data, a_opt, b_opt)

# Calculate R-squared
ss_res = np.sum((y_data - y_fit) ** 2)
ss_tot = np.sum((y_data - np.mean(y_data)) ** 2)
r_squared = 1 - (ss_res / ss_tot)

print(f"Fitted parameters: a = {a_opt:.6f}, b = {b_opt:.6f}")
print(f"R-squared: {r_squared:.6f}")

# Plot the data and the fitted curve
plt.scatter(x_data, y_data, label="Data", color="red")
plt.plot(x_data, y_fit, label="Fitted Saturation-Growth-Rate Curve", color="blue")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Saturation-Growth-Rate Curve Fitting")
plt.savefig('least-square-sat.png')
plt.show()
