import numpy as np
from scipy.sparse import random
import time


def print_time_in_engineering_units(time_in_seconds, label):
    """ print the time in engineering notation. """
    exponent = int(np.floor(np.log10(time_in_seconds) / 3) * 3)
    mantissa = time_in_seconds / (10 ** exponent)
    print(f"{label}: {mantissa:.3f}e{exponent:+03d} seconds")


def generate_random_sparse_matrix(N, density=0.1):
    """
    Generate a random sparse square matrix of size N x N.

    Parameters:
    N (int): Number of rows/columns.
    density (float): The density of the non-zero elements (default 0.1).

    Returns:
    sparse_matrix: A sparse matrix in CSR format.
    """
    # Generate a random sparse matrix with values between 0 and 1
    sparse_matrix = random(N, N, density=density,
                           format='csr', data_rvs=np.random.rand)

    return sparse_matrix


# Example usage:
N = 10000  # Set the size of the matrix
density = 0.2  # Set the density of the non-zero elements
sparse_matrix = generate_random_sparse_matrix(N, density)

# Convert sparse matrix to dense matrix and print it
dense_matrix = sparse_matrix.toarray()

# print(f"Random {N}x{N} sparse matrix (dense format):")
# print(dense_matrix)
start_time = time.time()
AT = np.transpose(sparse_matrix)
end_time = time.time()
print_time_in_engineering_units(
    end_time - start_time, "Time taken to build graph")
