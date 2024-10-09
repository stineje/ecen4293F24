import numpy as np

# Define a nearly singular matrix
A = np.array([
    [1, 1, 1],
    [2, 2.00001, 2],
    [3, 3, 3]
])

# Right-hand side vector
b = np.array([1, 2, 3])

# Compute the pseudo-inverse and solve the system
A_pinv = np.linalg.pinv(A)
x = A_pinv @ b

print("Pseudo-inverse of A:")
print(A_pinv)
print("\nSolution using pseudo-inverse:")
print(x)
