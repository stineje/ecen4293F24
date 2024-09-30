import numpy as np

# Define a 3x3 matrix
A = np.array([[4, 7, 2],
              [3, 6, 1],
              [2, 5, 8]])

# Check if the determinant is non-zero (matrix is invertible)
det = np.linalg.det(A)
if det == 0:
    print("Matrix is singular and not invertible")
else:
    # Compute the inverse of the matrix
    A_inv = np.linalg.inv(A)
    print("Inverse of matrix A:")
    print(A_inv)