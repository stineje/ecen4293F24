import numpy as np
import matplotlib.pyplot as plt

# Number of random points to generate
num_points = 10000

# Generate random points in the unit square (0, 0) to (1, 1)
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# Determine whether each point is inside the quarter circle (radius 1)
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
    f"Monte Carlo Simulation: Estimating π\nEstimated Value: {pi_estimate:.8f}")
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('random_mc1.png')
plt.show()
