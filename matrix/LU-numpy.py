import numpy as np
from scipy.linalg import lu

# Define the matrix A
A = np.array([[4, 3],
              [6, 3]])

# Perform LU decomposition using SciPy
P, L, U = lu(A)

# Display the results
print("Matrix A:\n", A)
print("\nP (Permutation Matrix):\n", P)
print("\nL (Lower Triangular Matrix):\n", L)
print("\nU (Upper Triangular Matrix):\n", U)

# Reconstruct A by multiplying P, L, and U
A_reconstructed = np.dot(P, np.dot(L, U))

print("\nReconstructed A (P * L * U):\n", A_reconstructed)
