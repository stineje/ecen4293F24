import numpy as np

# Define the matrix A
A = np.array([[4, 3],
              [6, 3]])

# Initialize L and U
L = np.identity(2)  # Identity matrix for L (since L has 1s in the diagonal)
U = np.zeros_like(A, dtype=float)  # Zero matrix for U

# Perform the decomposition manually
U[0, 0] = A[0, 0]  # First element of U is the first element of A
U[0, 1] = A[0, 1]  # Second element in first row of U is the same as A

# Calculate the multiplier for L
L[1, 0] = A[1, 0] / U[0, 0]  # L[1, 0] is A[1, 0] / U[0, 0]

# Calculate U[1, 1]
U[1, 1] = A[1, 1] - L[1, 0] * U[0, 1]  # The remaining element for U

# Display the results
print("Matrix A:\n", A)
print("\nL:\n", L)
print("\nU:\n", U)

# Verify that A = L * U
A_check = np.dot(L, U)
print("\nL * U:\n", A_check)
