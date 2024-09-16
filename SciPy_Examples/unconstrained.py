import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D  # Import 3D plotting toolkit

# Define the range for the variables
x0 = np.arange(0, 10, 0.25)
x1 = np.arange(0, 10, 0.25)

# Create a meshgrid for the variables
X0, X1 = np.meshgrid(x0, x1)


def objective_function(x):
    return 0.4 * x[0] ** 2 - 5 * x[0] + x[1] ** 2 - 6 * x[1]


# Calculate cost using the meshgrid values
cost = 0.4 * X0 ** 2 - 5 * X0 + X1 ** 2 - 6 * X1

# Create a 2D contour plot
fig, ax = plt.subplots(1, 1)

# Plot the contour of the cost function
cp = ax.contour(X0, X1, cost, levels=20)

# Optionally add a color bar to the plot
# fig.colorbar(cp)

# Set the font size for ticks
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

# Set figure size
fig = plt.gcf()
fig.set_size_inches(8, 8)

# Set labels for x and y axes
ax.set_xlabel(r'$x_{0}$', fontsize=20)
ax.set_ylabel(r'$x_{1}$', fontsize=20)

# Define the bounds for each decision variable
bounds = [(0, 10), (0, 10)]

# Initial guess for the decision variables
initial_guess = [0, 0]

# Perform the optimization
opt = minimize(objective_function, initial_guess,
               method='SLSQP', bounds=bounds)

# Extract the optimal solution
optimal_x0, optimal_x1 = opt.x

# Plot the solution on the contour plot
ax.plot(optimal_x0, optimal_x1, 'ro', markersize=10, label='Optimal Solution')

# Show the plot with the solution
plt.legend()
plt.show()

# Print the result of the optimization
print(opt)
