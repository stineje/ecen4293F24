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
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', label=f'Gaussian Distribution\nmean = {mean}, std dev = {std_dev}')

# Fill areas for 1, 2, and 3 standard deviations
plt.fill_between(x, y, where=(x >= mean - std_dev) & (x <= mean + std_dev), color='yellow', alpha=0.3, label='1σ (68%)')
plt.fill_between(x, y, where=(x >= mean - 2*std_dev) & (x <= mean + 2*std_dev), color='green', alpha=0.2, label='2σ (95%)')
plt.fill_between(x, y, where=(x >= mean - 3*std_dev) & (x <= mean + 3*std_dev), color='red', alpha=0.1, label='3σ (99.7%)')

# Add labels and title
plt.title('Gaussian (Normal) Distribution with 1, 2, and 3 Standard Deviations', fontsize=15)
plt.xlabel('x', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)

# Add grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.savefig('gaussian123.png')
plt.show()
