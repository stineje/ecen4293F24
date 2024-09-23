import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def power_law(x, a, b):
    return a * np.power(x, b)


# Generate synthetic data for demonstration
np.random.seed(0)  # For reproducibility
x_data = np.linspace(1, 10, 100)
a_actual = 2.5  # Actual value for parameter a
b_actual = 1.3  # Actual value for parameter b
y_data = power_law(x_data, a_actual, b_actual)

# Add some noise to the data
noise = 0.2 * np.random.normal(size=x_data.size)
y_data_noisy = y_data + noise

# Perform curve fitting
popt, pcov = curve_fit(power_law, x_data, y_data_noisy)
a_fitted, b_fitted = popt

# Print the fitted parameters
print(f"Fitted parameters: a = {a_fitted:.4f}, b = {b_fitted:.4f}")

# Plot original data and fitted curve
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data_noisy, label='Noisy data', color='orange')
plt.plot(x_data, power_law(x_data, a_fitted, b_fitted),
         label=f'Fitted curve: $y={a_fitted:.2f}x^{{{b_fitted:.2f}}}$', color='blue')
plt.plot(x_data, y_data, label='True curve', color='green', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Power Law Regression')
plt.savefig('least-square-power.png')
plt.show()
