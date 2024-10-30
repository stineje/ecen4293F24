import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Define some sample data points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 0, 1, 0, 1])  # A wave-like pattern

# Create a cubic spline function that interpolates the data points
spline = CubicSpline(x, y)

# Generate a dense range of x values for plotting the smooth spline curve
x_dense = np.linspace(0, 5, 100)
y_spline = spline(x_dense)

# Plot the original data points and the interpolated spline
plt.figure(figsize=(8, 4))
plt.plot(x_dense, y_spline, label="Cubic Spline Interpolation", color="blue")
plt.scatter(x, y, color="red", label="Data Points", zorder=5)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Cubic Spline Interpolation of Data Points")
plt.grid(True)
plt.show()
