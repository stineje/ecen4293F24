import numpy as np


def manual_lu_decomposition(A):
    # Get the number of rows (and columns) in the square matrix A
    n = A.shape[0]

    # Initialize L and U as zero matrices
    L = np.identity(n)  # L starts as the identity matrix
    U = np.zeros_like(A, dtype=float)  # U is initially a zero matrix

    # Perform the decomposition
    for i in range(n):
        # For U: Fill the ith row of U
        for k in range(i, n):
            U[i, k] = A[i, k] - sum(L[i, j] * U[j, k] for j in range(i))

        # For L: Fill the ith column of L
        for k in range(i+1, n):
            L[k, i] = (A[k, i] - sum(L[k, j] * U[j, i]
                       for j in range(i))) / U[i, i]

    return L, U


# Define the matrix A
A = np.array([[4, 3],
              [6, 3]])

# Perform manual LU decomposition
L, U = manual_lu_decomposition(A)

# Display the results
print("Matrix A:\n", A)
print("\nL (Lower Triangular Matrix):\n", L)
print("\nU (Upper Triangular Matrix):\n", U)

# Verify that A = L * U
A_reconstructed = np.dot(L, U)
print("\nReconstructed A (L * U):\n", A_reconstructed)
