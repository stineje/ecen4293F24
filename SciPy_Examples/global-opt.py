import numpy as np
from scipy.optimize import differential_evolution, NonlinearConstraint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Michalewicz function


def michalewicz(x, m=10):
    return -sum(np.sin(x[i]) * (np.sin((i + 1) * x[i]**2 / np.pi))**(2 * m) for i in range(len(x)))

# Define a nonlinear constraint: x1^2 + x2^2 <= 5


def constraint(x):
    return 5 - (x[0]**2 + x[1]**2)


# Set up the constraint
nonlinear_constraint = NonlinearConstraint(constraint, -np.inf, 0)

# Set the dimension of the problem
dimension = 2

# Define bounds for each dimension (typical range for the Michalewicz function)
bounds = [(0, np.pi) for _ in range(dimension)]

# Callback function to collect points during optimization for visualization
history = []


def callback(xk, convergence):
    history.append(xk)


# Perform global optimization using Differential Evolution with a constraint
result = differential_evolution(
    michalewicz,
    bounds,
    args=(10,),
    constraints=(nonlinear_constraint,),
    strategy='best1bin',
    maxiter=1000,
    popsize=15,
    callback=callback
)

print(f"Global minimum found at: {result.x}")
print(f"Function value at minimum: {result.fun:.4f}")
print(f"Number of iterations: {result.nit}")

# Visualization of the Michalewicz function for 2D

# 1. 3D Surface Plot
x = np.linspace(0, np.pi, 400)
y = np.linspace(0, np.pi, 400)
X, Y = np.meshgrid(x, y)
Z = np.array([[michalewicz([xx, yy]) for xx, yy in zip(x_row, y_row)]
             for x_row, y_row in zip(X, Y)])

fig = plt.figure(figsize=(15, 5))

# 3D Surface Plot
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)
ax1.scatter(result.x[0], result.x[1], result.fun,
            color='red', s=100, label='Optimal Solution')
ax1.set_title('3D Surface Plot of Michalewicz Function')
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('f(x1, x2)')
ax1.legend()

# 2. 2D Contour Plot with Feasible Region Highlighted
ax2 = fig.add_subplot(132)
contour = ax2.contourf(X, Y, Z, levels=50, cmap='viridis', alpha=0.8)
plt.colorbar(contour, ax=ax2, label='Michalewicz Function Value')

# Highlight feasible region
theta = np.linspace(0, 2 * np.pi, 100)
r = np.sqrt(5)
ax2.fill_between(r * np.cos(theta), r * np.sin(theta),
                 alpha=0.2, color='orange', label='Feasible Region')

ax2.scatter(result.x[0], result.x[1], color='red',
            marker='x', s=100, label='Optimal Solution')
ax2.set_title('Feasible Region and Contours')
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.legend()

# 3. Convergence Plot
ax3 = fig.add_subplot(133)
convergence = [michalewicz(point) for point in history]
ax3.plot(range(len(convergence)), convergence, marker='o', linestyle='-')
ax3.set_title('Convergence of Differential Evolution')
ax3.set_xlabel('Iteration')
ax3.set_ylabel('Function Value')
ax3.grid()

plt.tight_layout()
plt.savefig('global-opt.png')
plt.show()
