import numpy as np
import matplotlib.pyplot as plt

# Parameters
lambda_rate = 1.0  # Rate parameter (λ) for the exponential distribution
num_samples = 10000  # Number of samples to generate

# Generate random samples from an exponential distribution
samples = np.random.exponential(scale=1/lambda_rate, size=num_samples)

# Estimate the mean using Monte Carlo method
mean_estimate = np.mean(samples)

# Print the estimated mean and the theoretical mean
print(f"Estimated mean: {mean_estimate}")
print(f"Theoretical mean: {1/lambda_rate}")

# Plotting the histogram of the samples
plt.hist(samples, bins=50, density=True, alpha=0.6,
         color='g', label='Sampled Data')

# Plotting the theoretical exponential distribution for comparison
x = np.linspace(0, np.max(samples), 1000)
y = lambda_rate * np.exp(-lambda_rate * x)
plt.plot(x, y, 'r-', label=f'Theoretical PDF (λ={lambda_rate})')

plt.title('Monte Carlo Simulation: Exponential Distribution')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.savefig('random_mc_exp.png')
plt.show()
