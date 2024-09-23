import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def linear_model(x, m, c):
    return m * x + c


# Sample data: x and y values
x = np.array([10, 20, 30, 40, 50, 60, 70, 80])
y = np.array([25, 70, 380, 550, 610, 1220, 830, 1450])

# Use curve_fit to perform the least squares fit
# p_opt contains the optimal values for the parameters (m, c)
# p_cov is the covariance of the parameters (optional)
p_opt, p_cov = curve_fit(linear_model, x, y)

# Extract the fitted slope and intercept
m_fit, c_fit = p_opt

# Calculate the fitted y-values
y_fit = linear_model(x, m_fit, c_fit)

# Compute the residual sum of squares (SS_res)
ss_res = np.sum((y - y_fit) ** 2)

# Compute the total sum of squares (SS_tot)
y_mean = np.mean(y)
ss_tot = np.sum((y - y_mean) ** 2)

# Compute R-squared
r_squared = 1 - (ss_res / ss_tot)

# Output the result
print(f"R-squared: {r_squared:.6f}")

# Plot the original data points
plt.scatter(x, y, label='Data points')

# Plot the least-squares fit line
plt.plot(x, y_fit, color='red', label=f'Fit: y = {m_fit:.4f}x + {c_fit:.4f}')

# Add labels and a legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Fit using SciPy')
plt.legend()

# Show the plot
plt.savefig('least-square-linear2.png')
plt.show()
