import numpy as np

# Define a matrix A
A = np.array([[4, 3],
              [6, 3]])

# Get the number of rows and columns
num_rows, num_cols = A.shape

# Compute the rank of the matrix
rank = np.linalg.matrix_rank(A)

# Check if rows are linearly independent
if rank == num_rows:
    print("The rows of the matrix are linearly independent.")
else:
    print("The rows of the matrix are linearly dependent.")

# Check if columns are linearly independent
if rank == num_cols:
    print("The columns of the matrix are linearly independent.")
else:
    print("The columns of the matrix are linearly dependent.")
