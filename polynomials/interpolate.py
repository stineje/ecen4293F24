import numpy as np
from scipy.interpolate import lagrange

# Define the x and y values of known points
x_points = np.array([1, 2, 3, 4])
y_points = np.array([1, 4, 9, 16])

# Use Lagrange interpolation to construct the polynomial
polynomial = lagrange(x_points, y_points)
print("Interpolating Polynomial:", polynomial)
