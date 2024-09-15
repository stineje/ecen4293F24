import numpy as np
from scipy.optimize import minimize

# Define the function


def f(x):
    return (x - 3) ** 2


# Initial guess
starting_point = np.array([10.0])

# Run SciPy's minimize function with method="CG" (Conjugate Gradient)
result = minimize(f, starting_point, method='CG', tol=1e-6)

# Print the result
print(f"The minimum is at x = {result.x[0]}")
print(f"Number of iterations: {result.nit}")
print(f"Converged: {result.success}")
