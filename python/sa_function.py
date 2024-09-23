import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import dual_annealing

# Set the seed for reproducibility
np.random.seed(42)


def objective_function(x):
    """ Define the objective function """
    # Ensure x is treated as a 1D array
    return x[0]**2 + 10 * np.sin(5 * x[0]) + 7 * np.cos(4 * x[0])


# Define bounds for the search space
bounds = [-10, 10]


# Generate a range of x values within the bounds
x_values = np.linspace(bounds[0], bounds[1], 1000)

# Compute the corresponding y values using the objective function
y_values = [objective_function([x]) for x in x_values]

# Plot the objective function
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Objective Function')
# Optimal solution found from sa.py
optimal_x0 = 0.889458742389
optimal_y0 = -15.261841669878
plt.scatter(optimal_x0, optimal_y0, color='r', s=100, label='Optimal Solution')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the Objective Function')
plt.grid(True)
plt.legend()
plt.savefig('sa_function.png')
plt.show()
