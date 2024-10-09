import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import splu

# Example of a sparse matrix (in compressed sparse column format)
A = csc_matrix([[10, 0, 0, 0, 0, 0],
                [3, 9, 0, 0, 0, 0],
                [0, 7, 8, 7, 0, 0],
                [3, 0, 8, 7, 5, 0],
                [0, 8, 0, 9, 9, 13],
                [0, 4, 0, 0, 2, -1]])

# Define a right-hand side vector
b = np.array([6, 1, 14, 18, 24, 2])

# Perform LU factorization of the sparse matrix
lu = splu(A)

# Solve the system Ax = b
x = lu.solve(b)

print("Solution vector x:")
print(x)