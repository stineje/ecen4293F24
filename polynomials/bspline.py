import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

# Define control points for the B-spline
control_points = np.array([0, 1, 0, -1, 0, 1, 0])  # y-values of control points
x_control = np.arange(len(control_points))  # x-values for control points

# Define the degree of the spline (cubic spline)
degree = 3

# Generate a knot vector
n_control_points = len(control_points)
n_knots = n_control_points + degree + 1
knots = np.linspace(0, n_control_points - degree, n_knots - 2 * degree)
knots = np.concatenate(
    ([0] * degree, knots, [n_control_points - degree] * degree))

# Create the B-spline
spline = BSpline(knots, control_points, degree)

# Generate a dense set of x-values to plot a smooth curve
x_dense = np.linspace(0, n_control_points - degree, 100)
y_dense = spline(x_dense)

# Plot the control points and the B-spline curve
plt.figure(figsize=(8, 4))
plt.plot(x_dense, y_dense, label="B-spline Curve", color="blue")
plt.scatter(x_control, control_points, color="red",
            label="Control Points", zorder=5)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("B-spline Curve from Control Points")
plt.grid(True)
plt.show()
