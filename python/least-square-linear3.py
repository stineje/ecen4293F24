import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def linear_model(x, m, c):
    return m * x + c


# Sample data: x and y values
x = np.array([10, 20, 30, 40, 50, 60, 70, 80])
y = np.array([25, 70, 380, 550, 610, 1220, 830, 1450])

# Perform least squares fit using curve_fit
p_opt, p_cov = curve_fit(linear_model, x, y)

# Extract the fitted slope and intercept
m_fit, c_fit = p_opt

# Extract the standard deviations (square root of the diagonal of the covariance matrix)
m_err, c_err = np.sqrt(np.diag(p_cov))

# Calculate the fitted y-values
y_fit = linear_model(x, m_fit, c_fit)

# Generate upper and lower bounds for the fit based on the computed errors
# We'll use 1-sigma uncertainty for the error region
y_upper = linear_model(x, m_fit + m_err, c_fit + c_err)
y_lower = linear_model(x, m_fit - m_err, c_fit - c_err)

# Plot the original data points
plt.scatter(x, y, label='Data points')

# Plot the least-squares fit line
plt.plot(x, y_fit, color='red', label=f'Fit: y = {m_fit:.2f}x + {c_fit:.2f}')

# Plot the shaded area representing the uncertainty in the fit
plt.fill_between(x, y_lower, y_upper, color='gray',
                 alpha=0.3, label='Error band (1-sigma)')

# Show computed errors for slope and intercept in the plot's legend
plt.legend(title=f'Errors: m_err = {m_err:.2f}, c_err = {c_err:.2f}')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Fit with Computed Error Bands using SciPy')

# Show the plot
plt.savefig('least-square-linear3.png')
plt.show()
