import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt


def f(x):
    return x**3 - 6*x**2 + 4*x + 12


def f_prime(x):
    return 3*x**2 - 12*x + 4


def f_double_prime(x):
    return 6*x - 12


# Range for plotting the function
x = np.linspace(-2, 6, 400)
y = f(x)

# Reference root calculation using a precise method (brentq)
true_root = root_scalar(f, method='brentq', bracket=[-2, 2]).root

# List of methods and their respective settings
methods = {
    'bisect': {'method': 'bisect', 'bracket': [-2, 2]},
    'brentq': {'method': 'brentq', 'bracket': [-2, 2]},
    'brenth': {'method': 'brenth', 'bracket': [-2, 2]},
    'ridder': {'method': 'ridder', 'bracket': [-2, 2]},
    'toms748': {'method': 'toms748', 'bracket': [-2, 2]},
    'newton': {'method': 'newton', 'x0': 0, 'fprime': f_prime},
    'secant': {'method': 'secant', 'x0': -1.5, 'x1': 1},
    'halley': {'method': 'halley', 'x0': 0, 'fprime': f_prime, 'fprime2': f_double_prime}
}

# Dictionary to store roots, errors, and number of iterations
results = {}

# Finding roots using different methods and calculating errors
for method, params in methods.items():
    result = root_scalar(f, **params)
    root = result.root
    error = abs(root - true_root)  # Calculate absolute error
    iterations = result.iterations  # Number of iterations to converge
    results[method] = {'Root': root, 'Error': error, 'Iterations': iterations}

# Create subplots
fig, axes = plt.subplots(4, 2, figsize=(15, 12))
axes = axes.flatten()

# Plot each method in its own subplot
for i, (method, data) in enumerate(results.items()):
    root = data['Root']
    axes[i].plot(x, y, label=r'$f(x) = x^3 - 6x^2 + 4x + 12$', color='blue')
    axes[i].plot(root, f(root), 'o',
                 label=f'Root by {method}: {root:.4f}', color='red')
    axes[i].axhline(0, color='black', linestyle='--')
    axes[i].set_title(f'Root Finding using {method}')
    axes[i].set_xlabel('x')
    axes[i].set_ylabel('f(x)')
    axes[i].legend()
    axes[i].grid()

# Adjust layout
plt.tight_layout()
plt.savefig('finding-roots.png')
plt.show()

# Print results in a tabular format
print(f"{'Method':<10} {'Root':<15} {'Error':<15} {'Iterations':<10}")
print("-" * 75)
for method, data in results.items():
    print(
        f"{method:<10} {data['Root']:<15.15f} {data['Error']:<1.20e} {data['Iterations']:<10}")
