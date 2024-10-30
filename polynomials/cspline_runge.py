import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


def runge_function(x):
    """ Define the Runge function """
    return 1 / (1 + 25 * x**2)


# Generate a set of points to interpolate
x_points = np.linspace(-1, 1, 11)  # 11 evenly spaced points between -1 and 1
y_points = runge_function(x_points)

# Create a cubic spline to approximate the Runge function
# 'natural' boundary conditions
cspline = CubicSpline(x_points, y_points, bc_type='natural')

# Generate a dense range of x values for a smooth plot
x_dense = np.linspace(-1, 1, 500)
y_true = runge_function(x_dense)  # True Runge function values
y_cspline = cspline(x_dense)  # Cspline approximation values

# Plot the original Runge function and the cubic spline approximation
plt.figure(figsize=(10, 5))
plt.plot(x_dense, y_true, label="Runge Function", color="black", linewidth=2)
plt.plot(x_dense, y_cspline, label="Cubic Spline Approximation",
         linestyle="--", color="blue")
plt.scatter(x_points, y_points, color="red", label="Interpolation Points")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.title("Cubic Spline Approximation of the Runge Function")
plt.grid(True)
plt.show()
