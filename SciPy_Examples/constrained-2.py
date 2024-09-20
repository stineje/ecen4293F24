import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define the range for the variables
x0 = np.arange(0, 10, 0.25)
x1 = np.arange(0, 10, 0.25)

# Create a meshgrid for the variables
X0, X1 = np.meshgrid(x0, x1)

# Define the cost function


def objective_function(x):
    return 0.4 * x[0] ** 2 - 5 * x[0] + x[1] ** 2 - 6 * x[1]


# Calculate cost using the meshgrid values
cost = 0.4 * X0 ** 2 - 5 * X0 + X1 ** 2 - 6 * X1


def constraint1(x):
    x0 = x[0]
    x1 = x[1]
    # First constraint equation (should be >= 0)
    return x1 - 0.5 * x0 - 4


def constraint2(x):
    x0 = x[0]
    x1 = x[1]
    # Second constraint equation (should be >= 0)
    return x1 + 0.3 * x0 - 9


# Create a plot
fig, ax = plt.subplots(1, 1)

# Plot the contour of the cost function
cp = ax.contour(X0, X1, cost, levels=20)

# Plot the line of the first constraint (x1 = 0.5 * x0 + 4)
x_constraint1 = np.linspace(0, 10, 400)
y_constraint1 = 0.5 * x_constraint1 + 4
ax.plot(x_constraint1, y_constraint1, 'b-', linewidth=2,
        label='Constraint 1: $x_1 = 0.5x_0 + 4$')

# Plot the line of the second constraint (x1 = -0.3 * x0 + 9)
y_constraint2 = -0.3 * x_constraint1 + 9
ax.plot(x_constraint1, y_constraint2, 'g-', linewidth=2,
        label='Constraint 2: $x_1 = -0.3x_0 + 9$')

# Fill the infeasible region (below both constraints)
ax.fill_between(x_constraint1, y_constraint1, 0, color='red', alpha=0.3)
ax.fill_between(x_constraint1, y_constraint2, 0, color='red', alpha=0.3)

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

# Define constraints in a list of dictionaries format
cons = [{'type': 'ineq', 'fun': constraint1},
        {'type': 'ineq', 'fun': constraint2}]

# Perform the optimization with constraints
opt = minimize(objective_function, initial_guess,
               method='SLSQP', bounds=bounds, constraints=cons)

# Extract the optimal solution
optimal_x0, optimal_x1 = opt.x

# Plot the solution on the contour plot
ax.plot(optimal_x0, optimal_x1, 'ro', markersize=10,
        label='Optimal Solution with Constraints')

# Add a text label for the infeasible region
ax.text(4.5, 3, 'Infeasible', fontsize=20, color='black', ha='center')

# Show the plot with the solution
plt.legend()
plt.savefig('constrained-2.png')
plt.show()

# Print the result of the optimization
print(opt)
