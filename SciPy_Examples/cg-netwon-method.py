import numpy as np
from scipy.optimize import minimize


def f(x):
    return x[0]**3 - 6*x[0]**2 + 4*x[0] + 12


def objective(x):
    return f(x)**2


def gradient_f(x):
    return np.array([3*x[0]**2 - 12*x[0] + 4])


def gradient_objective(x):
    return 2 * f(x) * gradient_f(x)


def hessian_f(x):
    return np.array([[6*x[0] - 12]])


def hessian_objective(x):
    return 2 * (np.dot(gradient_f(x), gradient_f(x)) + f(x) * hessian_f(x))


# Initial guess (try different values to find different roots)
starting_point = np.array([0.0])

# Run SciPy's minimize function with method="Newton-CG"
result = minimize(objective, starting_point, jac=gradient_objective,
                  hess=hessian_objective, method='Newton-CG', tol=1e-6)

# Print the result
print(f"A root is approximately at x = {result.x[0]}")
print(f"Number of iterations: {result.nit}")
print(f"Converged: {result.success}")
