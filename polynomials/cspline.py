import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Define some sample data points (x, y) through which the spline will pass
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 0, 1, 0, 1])  # Sample wave-like pattern

# Create a cubic spline function that interpolates the data points
cspline = CubicSpline(x, y, bc_type='natural')  # Natural boundary conditions

# Generate a dense range of x values for a smooth curve
x_dense = np.linspace(0, 5, 500)
y_cspline = cspline(x_dense)  # Evaluate the spline at these points

# Plot the original data points and the interpolated cubic spline
plt.figure(figsize=(8, 4))
plt.plot(x_dense, y_cspline, label="Cubic Spline Interpolation", color="blue")
plt.scatter(x, y, color="red", label="Data Points", zorder=5)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Cubic Spline Interpolation of Data Points")
plt.grid(True)
plt.show()
