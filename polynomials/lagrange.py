import numpy as np
import matplotlib.pyplot as plt


def lagrange_interpolation(x_data, y_data, x):
    """ Evaluate the Lagrange interpolating polynomial at a specific x. """
    n = len(x_data)
    result = 0.0

    for i in range(n):
        # Calculate the Lagrange basis polynomial L_i(x)
        term = y_data[i]
        for j in range(n):
            if j != i:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result


# Example points
x_points = np.array([1., 4., 6., 5.])
y_points = np.log(x_points)

# Evaluate the polynomial at a new point, say x = 2.0
x_val = 2.0
y_val = lagrange_interpolation(x_points, y_points, x_val)
print(f"The interpolated value at x = {x_val} is y = {y_val:.18f}")

# Plotting the interpolation
# Range of x values for plotting
x_plot = np.linspace(min(x_points), max(x_points), 100)
y_plot = [lagrange_interpolation(x_points, y_points, x)
          for x in x_plot]  # Interpolated y values

plt.plot(x_plot, y_plot, label="Lagrange Interpolating Polynomial",
         color="blue")  # Plot interpolating polynomial
plt.scatter(x_points, y_points, color="red",
            label="Data Points")  # Plot original data points

plt.xlabel("x")
plt.ylabel("y")
plt.title("Lagrange Interpolating Polynomial")
plt.legend()
plt.grid(True)
plt.show()
