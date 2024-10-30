import numpy as np
import matplotlib.pyplot as plt


def f(x):
    """ Define the function of 1/x or reciprocal """
    return 1 / x


# Define the interval [1, 2) and number of subintervals
x_start = 1
x_end = 2
# Number of subintervals for the piecewise approximation
num_intervals = 10

# Generate subinterval points
x_points = np.linspace(x_start, x_end, num_intervals + 1, endpoint=False)
y_points = f(x_points)

# Generate a dense range of x values for the true function and piecewise approximation
x_dense = np.linspace(x_start, x_end, 500, endpoint=False)
y_true = f(x_dense)

# Calculate the piecewise linear approximation
y_piecewise = np.interp(x_dense, x_points, y_points)

# Plot the true function and the piecewise approximation
plt.figure(figsize=(10, 6))
plt.plot(x_dense, y_true, label="True Function $f(x) = 1/x$",
         color='black', linewidth=2)
plt.plot(x_dense, y_piecewise, label="Piecewise Linear Approximation",
         linestyle='--', color='red')
plt.scatter(x_points, y_points, color='blue', label="Interpolation Points")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.title("Piecewise Linear Approximation of $f(x) = 1/x$ on [1, 2)")
plt.grid(True)
plt.show()
