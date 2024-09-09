import numpy as np
import matplotlib.pyplot as plt

import numpy as np

# Define the function and step size


def f(x):
    return np.cos(x)


step_size = 0.1
x_values = np.arange(0, 2 * np.pi, step_size)

# Compute the forward difference
forward_diff = (f(x_values + step_size) - f(x_values)) / step_size

# Compute the central difference
central_diff = (f(x_values + step_size) -
                f(x_values - step_size)) / (2 * step_size)

# Compute the backward difference
backward_diff = (f(x_values) - f(x_values - step_size)) / step_size

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(x_values, -np.sin(x_values),
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
plt.show()
