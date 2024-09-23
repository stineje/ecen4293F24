import numpy as np
import matplotlib.pyplot as plt

# Generate random data following a uniform distribution
# Parameters: low = 0, high = 1, size = 10000 (number of samples)
data = np.random.uniform(low=0.0, high=1.0, size=10000)

# Create a histogram of the data
plt.figure(figsize=(8, 6))
plt.hist(data, bins=50, density=True, color='blue',
         alpha=0.7, edgecolor='black')

# Add title and labels
plt.title('Uniform Distribution (0, 1)')
plt.xlabel('Value')
plt.ylabel('Density')

# Show grid
plt.grid(True)

# Display the plot
plt.savefig('dist-uniform.png')
plt.show()
