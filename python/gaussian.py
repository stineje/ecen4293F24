import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the Gaussian distribution
mean = 0      # Mean of the distribution
std_dev = 1   # Standard deviation of the distribution

# Generate a range of x values from -4σ to +4σ
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)

# Compute the corresponding y values for the Gaussian distribution
y = norm.pdf(x, mean, std_dev)

# Plot the Gaussian distribution
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='blue', label=f'Gaussian Distribution\nmean = {mean}, std dev = {std_dev}')

# Add labels and title
plt.title('Gaussian (Normal) Distribution', fontsize=15)
plt.xlabel('x', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)

# Add grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.savefig('dist-gaussian.png')
plt.show()