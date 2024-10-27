import numpy as np
import matplotlib.pyplot as plt


def divided_differences(x, y):
    """ Calculate the divided difference coefficients for Newton's interpolation. """
    n = len(y)
    coef = np.copy(y).astype(float)  # Initial coefficients are the y-values

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])

    return coef


def newton_interpolation(x_data, y_data, x):
    """ Evaluate Newton's interpolating polynomial at a specific x. """
    # Calculate divided differences
    coef = divided_differences(x_data, y_data)
    n = len(coef)

    # Evaluate the polynomial using the Newton form
    result = coef[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x - x_data[i]) + coef[i]

    return result


# Points
x_points = np.array([1., 4., 6., 5.])
y_points = np.log(x_points)


# Polynomial coefficients based on divided differences
coefficients = divided_differences(x_points, y_points)
print("Divided Difference Coefficients:", coefficients)

# Evaluate the polynomial at a new point, say x = 2.0
x_val = 2.0
y_val = newton_interpolation(x_points, y_points, x_val)
print(f"The interpolated value at x = {x_val} is y = {y_val:.18f}")

# Plotting the interpolation
# Range of x values for plotting
x_plot = np.linspace(min(x_points), max(x_points), 100)
y_plot = [newton_interpolation(x_points, y_points, x)
          for x in x_plot]  # Interpolated y values

plt.plot(x_plot, y_plot, label="Newton Interpolating Polynomial",
         color="blue")  # Plot interpolating polynomial
plt.scatter(x_points, y_points, color="red",
            label="Data Points")  # Plot original data points

plt.xlabel("x")
plt.ylabel("y")
plt.title("Newton Interpolating Polynomial")
plt.legend()
plt.grid(True)
plt.show()
