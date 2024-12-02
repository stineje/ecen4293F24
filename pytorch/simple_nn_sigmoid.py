import numpy as np

# Define weights, input, and bias
w = np.array([0.2, 0.3, 0.9])
x = np.array([0.5, 0.6, 0.1])
b = 0.5  # Default bias

# Dot product of w and x
z = np.dot(w, x) + b

# Sigmoid activation function
sigma = 1 / (1 + np.exp(-z))

# Output
print("y =", sigma)
