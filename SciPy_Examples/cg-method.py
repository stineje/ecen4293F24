import numpy as np
from scipy.optimize import minimize


def f(x):
    return x**3 - 6*x**2 + 4*x + 12


def objective(x):
    return f(x)**2


# Run SciPy's minimize function with method="CG" (Conjugate Gradient)
result = minimize(objective, x0=0.0, method='CG', tol=1e-6)

# Print the result
print(f"The minimum is at x = {result.x[0]}")
print(f"Number of iterations: {result.nit}")
print(f"Converged: {result.success}")
