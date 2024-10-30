import numpy as np
import matplotlib.pyplot as plt

# Given data points
data_points = np.array([
    (0, 0.5),
    (1, 3.134),
    (2, 5.3),
    (5.5, 9.9),
    (11, 10.2),
    (13, 9.35),
    (16, 7.2),
    (18, 6.2)
])

# Step 1: Sort points around x = 8 to maximize interpolation accuracy
# Sort by the distance from x = 8
centered_data_points = data_points[np.argsort(abs(data_points[:, 0] - 8))]


def divided_differences(x, y):
    """ Function to calculate divided differences """
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i]
                          [j - 1]) / (x[i + j] - x[i])
    return coef[0]


def newton_polynomial(coef, x_data, x):
    """ Function to calculate Newton's interpolating polynomial at x = 8 """
    n = len(coef) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p


# Compute finite divided differences and interpolate with optimal ordering
x_centered = centered_data_points[:, 0]
y_centered = centered_data_points[:, 1]
coef_centered = divided_differences(x_centered, y_centered)
estimate_centered = newton_polynomial(coef_centered, x_centered, 8)

# Compute finite divided differences and interpolate with original ordering
x_original = data_points[:, 0]
y_original = data_points[:, 1]
coef_original = divided_differences(x_original, y_original)
estimate_original = newton_polynomial(coef_original, x_original, 8)

# Plotting the results
x_vals = np.linspace(0, 18, 200)
y_centered_vals = [newton_polynomial(
    coef_centered, x_centered, xv) for xv in x_vals]
y_original_vals = [newton_polynomial(
    coef_original, x_original, xv) for xv in x_vals]

plt.figure(figsize=(12, 6))
plt.plot(x_vals, y_centered_vals,
         label='Centered Data Interpolation', linestyle='--')
plt.plot(x_vals, y_original_vals,
         label='Original Order Interpolation', linestyle=':')
plt.scatter(data_points[:, 0], data_points[:, 1],
            color='red', label='Data Points')
plt.scatter(8, estimate_centered, color='blue',
            label=f'Estimate (Centered): {estimate_centered:.4f}', marker='x')
plt.scatter(8, estimate_original, color='green',
            label=f'Estimate (Original): {estimate_original:.4f}', marker='x')
plt.legend()
plt.xlabel('x')
plt.ylabel('Interpolated y')
plt.title('Newton Interpolation Comparison at x = 8')
plt.grid(True)
plt.show()

estimate_centered, estimate_original
