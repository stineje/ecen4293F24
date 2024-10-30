import numpy as np
import matplotlib.pyplot as plt


def runge_function(x):
    """ Define Runge's function """
    return 1 / (1 + 25 * x**2)


# Generate 50 equally spaced x values in the range [-1, 1]
x = np.linspace(-1, 1, 50)
y = runge_function(x)

# Fit a 4th-order polynomial to the Runge function data
coef = np.polyfit(x, y, 4)
poly = np.poly1d(coef)

# Generate a dense range for plotting the true function and the polynomial fit
x_dense = np.linspace(-1, 1, 500)
y_true = runge_function(x_dense)
y_poly = poly(x_dense)

# Plot the original Runge's function and the 4th-order polynomial fit
plt.figure(figsize=(10, 6))
plt.plot(x_dense, y_true, label="Runge's Function", color='black', linewidth=2)
plt.plot(x_dense, y_poly, label="4th-Order Polynomial Fit",
         linestyle='--', color='red')
plt.scatter(x, y, color='blue', s=20, label="Data Points")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Interpolation of Runge's Function using a 4th-Order Polynomial")
plt.grid(True)
plt.show()
