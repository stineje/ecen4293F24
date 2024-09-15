import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt


def f(x):
    return x**3 - 6*x**2 + 4*x + 12


def f_prime(x):
    return 3*x**2 - 12*x + 4


# Find the root using Newton's method
result = root_scalar(f, method='newton', x0=0, fprime=f_prime)

# Plot the function and root
x = np.linspace(-2, 6, 400)
y = f(x)
plt.plot(x, y, label=r'$f(x) = x^3 - 6x^2 + 4x + 12$', color='blue')
plt.plot(result.root, f(result.root), 'o',
         label=f'Root: {result.root:.4f}', color='red')
plt.axhline(0, color='black', linestyle='--')
plt.title("Root Finding using Newton's Method")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.savefig('netwons-method.png')
plt.show()

# Print the result
print(f"Root found by Newton method: {result.root:.6f}")
print(
    f"Error: {abs(result.root - root_scalar(f, method='brentq', bracket=[-2, 2]).root):1.15e}")
print(f"Iterations: {result.iterations}")
