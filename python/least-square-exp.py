import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def exponential_model(x, a, b):
    return a * np.exp(b * x)


# Generate synthetic data (for demonstration purposes)
np.random.seed(0)  # For reproducibility
x_data = np.linspace(0, 4, 50)
y_data = 2.5 * np.exp(1.3 * x_data) + np.random.normal(size=x_data.size)

# Perform exponential curve fitting
p_opt, p_cov = curve_fit(exponential_model, x_data, y_data)

# Extract the optimal parameters
a_opt, b_opt = p_opt

# Generate y values using the fitted model
y_fit = exponential_model(x_data, a_opt, b_opt)

# Calculate R-squared
ss_res = np.sum((y_data - y_fit) ** 2)
ss_tot = np.sum((y_data - np.mean(y_data)) ** 2)
r_squared = 1 - (ss_res / ss_tot)

print(f"Fitted parameters: a = {a_opt:.4f}, b = {b_opt:.4f}")
print(f"R-squared: {r_squared:.6f}")

# Plot the data and the fitted curve
plt.scatter(x_data, y_data, label="Data", color="red")
plt.plot(x_data, y_fit, label="Fitted exponential curve", color="blue")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Exponential Curve Fitting")
plt.savefig('least-square-exp.png')
plt.show()
