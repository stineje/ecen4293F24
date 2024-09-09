import numpy as np
import matplotlib.pyplot as plt


def f(x):
    """
        function to plot
    """
    return np.cos(x)


def df_analytical(x):
    """
        derivative of function to plot
    """
    return -np.sin(x)


# Set the step size and x values
step_size = 0.1
x_values = np.arange(0, 2 * np.pi, step_size)

# Compute the forward, central, and backward differences
forward_diff = (f(x_values + step_size) - f(x_values)) / step_size
central_diff = (f(x_values + step_size) -
                f(x_values - step_size)) / (2 * step_size)
backward_diff = (f(x_values) - f(x_values - step_size)) / step_size

# Compute the analytical derivative
analytical_derivative = df_analytical(x_values)

# Compute the absolute errors
error_forward = np.abs(analytical_derivative - forward_diff)
error_central = np.abs(analytical_derivative - central_diff)
error_backward = np.abs(analytical_derivative - backward_diff)

# Plotting the derivatives
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(x_values, analytical_derivative,
         label='Analytical Derivative (-sin(x))', color='black', linestyle='dashed')
plt.plot(x_values, forward_diff, label='Forward Difference',
         marker='o', linestyle='-', alpha=0.7)
plt.plot(x_values, central_diff, label='Central Difference',
         marker='x', linestyle='-', alpha=0.7)
plt.plot(x_values, backward_diff, label='Backward Difference',
         marker='s', linestyle='-', alpha=0.7)

plt.title('Numerical Derivatives of cos(x)')
plt.xlabel('x')
plt.ylabel('Derivative')
plt.legend()
plt.grid(True)

# Plotting the absolute errors
plt.subplot(1, 2, 2)
plt.plot(x_values, error_forward, label='Absolute Error (Forward)',
         marker='o', linestyle='-', alpha=0.7)
plt.plot(x_values, error_central, label='Absolute Error (Central)',
         marker='x', linestyle='-', alpha=0.7)
plt.plot(x_values, error_backward, label='Absolute Error (Backward)',
         marker='s', linestyle='-', alpha=0.7)

plt.title('Absolute Errors of Numerical Derivatives')
plt.xlabel('x')
plt.ylabel('Absolute Error')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
