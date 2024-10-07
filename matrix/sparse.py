import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import random, csr_matrix

# Create a random sparse matrix (CSR format) with size 1000x1000
rows, cols = 1000, 1000
density = 0.01  # 1% non-zero elements
sparse_matrix_large = random(rows, cols, density=density, format='csr')

# Plot the larger sparse matrix using matplotlib
plt.figure(figsize=(8, 8))
# Adjust markersize for better visibility
plt.spy(sparse_matrix_large, markersize=1)
plt.title('Sparse Matrix Structure (1000x1000)')
plt.savefig('sparse.png')
plt.show()
