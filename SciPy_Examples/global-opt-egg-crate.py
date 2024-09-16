import numpy as np
from scipy.optimize import differential_evolution
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def egg_crate(x):
    """
      egg crate function
    """
    return x[0]**2 + x[1]**2 + 25 * (np.sin(x[0])**2 + np.sin(x[1])**2)


# Define the bounds for x and y
bounds = [(-5, 5), (-5, 5)]

# Callback function to collect points during optimization for visualization
history = []


def callback(xk, convergence):
    history.append(xk)


# Perform global optimization using Differential Evolution
result = differential_evolution(
    egg_crate,
    bounds,
    strategy='best1bin',
    maxiter=1000,
    popsize=15,
    callback=callback
)

print(f"Global minimum found at: {result.x}")
print(f"Function value at minimum: {result.fun:.4f}")
print(f"Number of iterations: {result.nit}")

# Visualization of the Egg Crate function for 2D

# 1. 3D Surface Plot
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
Z = np.array([[egg_crate([xx, yy]) for xx, yy in zip(x_row, y_row)]
             for x_row, y_row in zip(X, Y)])

fig = plt.figure(figsize=(15, 5))

# 3D Surface Plot
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)
ax1.scatter(result.x[0], result.x[1], result.fun,
            color='red', s=100, label='Optimal Solution')
ax1.set_title('3D Surface Plot of Egg Crate Function')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x, y)')
ax1.legend()

# 2. 2D Contour Plot
ax2 = fig.add_subplot(132)
contour = ax2.contourf(X, Y, Z, levels=50, cmap='viridis', alpha=0.8)
plt.colorbar(contour, ax=ax2, label='Egg Crate Function Value')

ax2.scatter(result.x[0], result.x[1], color='red',
            marker='x', s=100, label='Optimal Solution')
ax2.set_title('Contours of Egg Crate Function')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.legend()

# 3. Convergence Plot
ax3 = fig.add_subplot(133)
convergence = [egg_crate(point) for point in history]
ax3.plot(range(len(convergence)), convergence, marker='o', linestyle='-')
ax3.set_title('Convergence of Differential Evolution')
ax3.set_xlabel('Iteration')
ax3.set_ylabel('Function Value')
ax3.grid()

plt.tight_layout()
plt.savefig('global-opt-egg-crate.png')
plt.show()
