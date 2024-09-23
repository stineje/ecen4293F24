import numpy as np
import matplotlib.pyplot as plt

# Generate random data following an exponential distribution
# Scale parameter (1/lambda): scale = 1.0, size = 10000 (number of samples)
data = np.random.exponential(scale=1.0, size=10000)

# Create a histogram of the data
plt.figure(figsize=(8, 6))
plt.hist(data, bins=50, density=True, color='green',
         alpha=0.7, edgecolor='black')

# Overlay the theoretical probability density function (PDF) for comparison
x = np.linspace(0, np.max(data), 1000)
pdf = (1.0/1.0) * np.exp(-x/1.0)  # Exponential PDF with lambda = 1/scale

plt.plot(x, pdf, 'r-', lw=2, label='Exponential PDF')

# Add title and labels
plt.title('Exponential Distribution (scale=1.0)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()

# Show grid
plt.grid(True)

# Display the plot
plt.savefig('dist-exp.png')
plt.show()
