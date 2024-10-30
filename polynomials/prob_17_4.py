import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Given data points
data_points = np.array([
    (1, 4.75),
    (2, 4),
    (3, 5.25),
    (5, 19.75),
    (6, 36)
])

# Separate x and y values
x_data = data_points[:, 0]
y_data = data_points[:, 1]

# Target x value
x_target = 4


def divided_differences(x, y):
    """ Function to calculate divided difference for Newton's method """
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i]
                          [j - 1]) / (x[i + j] - x[i])
    return coef[0]


def newton_polynomial(coef, x_data, x):
    """ Function to evaluate Newton's polynomial """
    n = len(coef) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p


# Store results for plotting
orders = [1, 2, 3, 4]
newton_estimates = []
lagrange_estimates = []

# Select closest points around x=4 for orders 1 through 4
for order in orders:
    indices = np.argsort(np.abs(x_data - x_target))[:order + 1]
    x_selected = x_data[indices]
    y_selected = y_data[indices]

    # Newton's method
    coef = divided_differences(x_selected, y_selected)
    newton_estimates.append(newton_polynomial(coef, x_selected, x_target))

    # Lagrange method
    lagrange_poly = lagrange(x_selected, y_selected)
    lagrange_estimates.append(lagrange_poly(x_target))

# Plotting the results for both methods
plt.figure(figsize=(10, 6))

# Generating smooth plots of the interpolating polynomials
x_vals = np.linspace(min(x_data), max(x_data), 200)
for i, order in enumerate(orders):
    # Newton interpolation polynomial values
    indices = np.argsort(np.abs(x_data - x_target))[:order + 1]
    x_selected = x_data[indices]
    y_selected = y_data[indices]
    coef = divided_differences(x_selected, y_selected)
    y_newton_vals = [newton_polynomial(coef, x_selected, xv) for xv in x_vals]

    # Lagrange interpolation polynomial values
    lagrange_poly = lagrange(x_selected, y_selected)
    y_lagrange_vals = lagrange_poly(x_vals)

    plt.plot(x_vals, y_newton_vals, linestyle='--',
             label=f"Newton Order {order}")
    plt.plot(x_vals, y_lagrange_vals, linestyle=':',
             label=f"Lagrange Order {order}")

# Plotting the data points and the estimate at x=4
plt.scatter(x_data, y_data, color='red', label="Data Points")
plt.scatter([x_target] * 4, newton_estimates, color='blue',
            marker='x', label="Newton Estimates at x=4")
plt.scatter([x_target] * 4, lagrange_estimates, color='green',
            marker='o', label="Lagrange Estimates at x=4")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Newton and Lagrange Polynomial Interpolation at x = 4")
plt.legend()
plt.grid(True)
plt.show()

# Print the estimates with more detail
print("Newton Estimates at x=4:")
for i, estimate in enumerate(newton_estimates, start=1):
    print(f"Order {i}: {estimate:.6f}")

print("\nLagrange Estimates at x=4:")
for i, estimate in enumerate(lagrange_estimates, start=1):
    print(f"Order {i}: {estimate:.6f}")
