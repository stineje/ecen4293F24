import numpy as np
import matplotlib.pyplot as plt

# Define the high-precision data points
data_points_precise = np.array([
    (0, 26),
    (1.8, 16.415),
    (5, 5.375),
    (6, 3.5),
    (8.2, 2.015),
    (9.2, 2.54),
    (12, 8)
])

# Separate x and y values
x = data_points_precise[:, 0]
y = data_points_precise[:, 1]

# Plot the data points
plt.scatter(x, y, c='k', label="Data Points")
plt.grid()
plt.xlabel('x')
plt.ylabel('y')

# Fit a polynomial of degree 2 (quadratic) to the data points
coef = np.polyfit(x, y, 2)

# Generate x values for plotting the polynomial fit
xplot = np.linspace(0., 12., 200)
# Evaluate the polynomial at the xplot points
yplot = np.polyval(coef, xplot)

# Plot the polynomial fit
plt.plot(xplot, yplot, c='k', linestyle='--', label="Quadratic Fit")
plt.legend()

# Calculate the residuals (errors) of the polynomial fit at the original x points
yp = np.polyval(coef, x)
yerr = y - yp

# Display the plot
plt.show()

# Print the residuals (errors) with 6 decimal places
print("Residuals (y - y_pred):")
for i, err in enumerate(yerr):
    print(f"x = {x[i]:.3}, Residual = {err:.8e}, Bits = {np.log2(abs(err))}")

# Calculate and print the interpolated value at x = 3.5 with 6 decimal places
yint = np.polyval(coef, 3.5)
print(f"Interpolated value at x = 3.5: {yint:.15f}")
