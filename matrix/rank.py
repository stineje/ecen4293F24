import numpy as np

# Define a matrix A
A = np.array([[4, 3],
              [6, 3]])

# Compute the rank of the matrix
rank = np.linalg.matrix_rank(A)

print("Rank of matrix A:", rank)
