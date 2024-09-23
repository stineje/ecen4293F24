import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import dual_annealing

# Set the seed for reproducibility
np.random.seed(42)


def objective_function(x):
    """ Define the objective function """
    return x[0]**2 + 10 * np.sin(5 * x[0]) + 7 * np.cos(4 * x[0])


# Define bounds for the search space
bounds = [(-10, 10)]

# Define a custom callback function to capture the function values
objective_values = []


def callback(x, f, context):
    """
    Callback function to capture the function values during the optimization.
    """
    objective_values.append(f)
    print(f"Iteration: {len(objective_values)}, x: {
          x[0]:.12f}, f(x): {f:.12f}")


# Perform the simulated annealing using SciPy's dual_annealing function
result = dual_annealing(objective_function, bounds, callback=callback, seed=42)

# Extract the best solution
best_x = result.x
best_f = result.fun

print(f"\nBest solution found: x = {best_x[0]:.12f}, f(x) = {best_f:.12f}")

# Plot the objective function values over iterations
plt.figure(figsize=(8, 6))

plt.plot(objective_values, label='Objective Function Value', color='orange')
plt.xlabel('Iteration')
plt.ylabel('Objective Function Value')
plt.title('Objective Function Value over Iterations')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('sa.png')
plt.show()
