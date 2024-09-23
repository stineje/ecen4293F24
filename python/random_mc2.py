import numpy as np
import matplotlib.pyplot as plt

# Number of random points to generate
num_points = 10000

# Generate random points in the unit square (-1, -1) to (1, 1)
x = 2 * np.random.rand(num_points) - 1  # x coordinates from -1 to 1
y = 2 * np.random.rand(num_points) - 1  # y coordinates from -1 to 1

# Determine whether each point is inside the circle (radius 1, centered at origin)
inside_circle = x**2 + y**2 <= 1.0

# Estimate the value of pi (π) using the ratio of points inside the circle to total points
pi_estimate = 4 * np.sum(inside_circle) / num_points

# Print the estimated value of π
print(f"Estimated value of π: {pi_estimate}")

# Plotting the results
plt.figure(figsize=(6, 6))
plt.scatter(x[inside_circle], y[inside_circle], color='black', s=1)
plt.scatter(x[~inside_circle], y[~inside_circle], color='orange', s=1)
plt.title(
    f"Monte Carlo Simulation: Estimating π\nEstimated Value: {pi_estimate:.12f}")
plt.xlabel('x')
plt.ylabel('y')

# Set the limits of the plot to display the entire circle
plt.xlim(-1, 1)
plt.ylim(-1, 1)

# Ensure the plot has equal aspect ratio
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('random_mc2.png')
plt.show()
