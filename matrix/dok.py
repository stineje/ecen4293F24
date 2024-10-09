import numpy as np
from scipy.sparse import dok_matrix

# Parameters
rows, cols = 4, 4
density = 0.25  # 25% non-zero entries

# Create an empty DOK matrix and populate it with random values
dok = dok_matrix((rows, cols), dtype=np.float64)

# Manually add random entries to the DOK matrix
for _ in range(int(rows * cols * density)):  # Number of non-zero elements
    i = np.random.randint(0, rows)
    j = np.random.randint(0, cols)
    # Random value from standard normal distribution
    dok[i, j] = np.random.randn()

print("DOK Matrix:\n", dok)
