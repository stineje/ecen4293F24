import numpy as np
import matplotlib.pyplot as plt

# Generate random data following a Gaussian (normal) distribution
# Mean (mu) = 0, Standard Deviation (sigma) = 1, size = 10000 (number of samples)
mu = 0
sigma = 1
data = np.random.normal(loc=mu, scale=sigma, size=10000)

# Create a histogram of the data
plt.figure(figsize=(8, 6))
plt.hist(data, bins=50, density=True, color='blue',
         alpha=0.7, edgecolor='black')

# Overlay the theoretical probability density function (PDF) for comparison
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
pdf = (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(- (x - mu)**2 / (2 * sigma**2))

plt.plot(x, pdf, 'r-', lw=2, label='Gaussian PDF')

# Add title and labels
plt.title('Gaussian (Normal) Distribution (μ=0, σ=1)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()

# Show grid
plt.grid(True)

# Display the plot
plt.savefig('dist-gaussian.png')
plt.show()
