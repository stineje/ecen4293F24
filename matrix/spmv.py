import numpy as np
from scipy.sparse import random as sparse_random
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, dok_matrix
import time


def compute_flops_spmv(M, N, density=0.01, alpha=1.0):
    """
    Compute the FLOPS of sparse matrix-vector multiplication for different sparse formats.

    Parameters:
    M (int): Number of rows of the matrix.
    N (int): Number of columns of the matrix (length of the vector).
    density (float): The density of the non-zero elements in the sparse matrix.
    alpha (float): Scalar multiplier for the matrix-vector product.

    Returns:
    flops_dict: Dictionary of FLOPS for different formats (dense, CSR, CSC, COO, DOK).
    time_dict: Dictionary of time taken for SpMV in each format.
    """
    # Generate a random sparse matrix A (MxN)
    A_csr = sparse_random(M, N, density=density,
                          format='csr', data_rvs=np.random.rand)

    # Convert CSR matrix to other formats
    A_csc = csc_matrix(A_csr)
    A_coo = coo_matrix(A_csr)
    A_dok = dok_matrix(A_csr)

    # Generate a random dense vector of size N
    x = np.random.rand(N)

    # Generate the dense matrix from the sparse one
    A_dense = A_csr.toarray()

    # Define a function to measure time and compute FLOPS
    def measure_time_and_flops(A, x, format_name, sparse=False):
        start_time = time.time()
        # Perform the matrix-vector multiplication: y = alpha * A.dot(x)
        if sparse:
            y = alpha * A.dot(x)  # Sparse matrix-vector multiplication
        else:
            y = alpha * np.dot(A, x)  # Dense matrix-vector multiplication
        end_time = time.time()

        # Time taken for the operation
        time_taken = end_time - start_time

        # Compute the number of floating-point operations: 2 * M * N (one multiplication and one addition per element)
        flops = (2 * M * N * density) / time_taken

        return flops, time_taken

    # Perform matrix-vector multiplication and calculate FLOPS for different formats

    # Dense matrix-vector multiplication
    dense_flops, dense_time = measure_time_and_flops(
        A_dense, x, 'Dense', sparse=False)

    # Sparse formats: CSR, CSC, COO, DOK
    csr_flops, csr_time = measure_time_and_flops(A_csr, x, 'CSR', sparse=True)
    csc_flops, csc_time = measure_time_and_flops(A_csc, x, 'CSC', sparse=True)
    coo_flops, coo_time = measure_time_and_flops(A_coo, x, 'COO', sparse=True)
    dok_flops, dok_time = measure_time_and_flops(A_dok, x, 'DOK', sparse=True)

    # Store the FLOPS and times for each format in dictionaries
    flops_dict = {
        'Dense': dense_flops,
        'CSR': csr_flops,
        'CSC': csc_flops,
        'COO': coo_flops,
        'DOK': dok_flops
    }

    time_dict = {
        'Dense': dense_time,
        'CSR': csr_time,
        'CSC': csc_time,
        'COO': coo_time,
        'DOK': dok_time
    }

    return flops_dict, time_dict


# Example usage:
M, N = 1000, 1000  # Matrix size (MxN) where N is the length of the vector
density = 0.01  # 1% non-zero elements (sparse matrix)
flops_dict, time_dict = compute_flops_spmv(M, N, density)

# Print results
for format_name in flops_dict:
    print(f"{format_name} format:")
    print(f"  Time taken: {time_dict[format_name]:.6f} seconds")
    print(f"  FLOPS: {flops_dict[format_name]:.2e} FLOPS")
