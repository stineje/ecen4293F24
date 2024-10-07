import numpy as np
from scipy.sparse import random as sparse_random
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, dok_matrix
import time


def compute_flops_gemm(M, N, K, density=0.01, alpha=1.0, beta=1.0):
    """
    Compute the FLOPS of GEMM for both sparse and dense matrices.

    Parameters:
    M (int): Number of rows of matrix A and C.
    N (int): Number of columns of matrix B and C.
    K (int): Number of columns of matrix A and rows of matrix B.
    density (float): The density of the non-zero elements in the sparse matrix.
    alpha (float): Scalar multiplier for the product of A and B.
    beta (float): Scalar multiplier for the matrix C.

    Returns:
    flops_dict: Dictionary of FLOPS for different formats (dense, CSR, CSC, COO, DOK).
    time_dict: Dictionary of time taken for GEMM in each format.
    """
    # Generate random sparse matrices A (MxK) and B (KxN)
    A_csr = sparse_random(M, K, density=density,
                          format='csr', data_rvs=np.random.rand)
    B_csr = sparse_random(K, N, density=density,
                          format='csr', data_rvs=np.random.rand)

    # Convert CSR matrices to other formats
    A_csc = csc_matrix(A_csr)
    B_csc = csc_matrix(B_csr)

    A_coo = coo_matrix(A_csr)
    B_coo = coo_matrix(B_csr)

    A_dok = dok_matrix(A_csr)
    B_dok = dok_matrix(B_csr)

    # Generate random dense matrix C for sparse formats and dense format
    C = np.random.rand(M, N)

    # Dense GEMM
    A_dense = A_csr.toarray()
    B_dense = B_csr.toarray()

    # Define a function to measure time and compute FLOPS
    def measure_time_and_flops(A, B, C, format_name, sparse=False):
        start_time = time.time()
        # Perform GEMM operation: C = alpha * A.dot(B) + beta * C
        if sparse:
            result = alpha * A.dot(B) + beta * C  # Sparse matrices
        else:
            result = alpha * np.dot(A, B) + beta * C  # Dense matrices
        end_time = time.time()

        # Time taken for the operation
        time_taken = end_time - start_time

        # Compute the number of floating-point operations: 2 * M * N * K
        flops = (2 * M * N * K) / time_taken

        return flops, time_taken

    # Perform GEMM and calculate FLOPS for different formats

    # Traditional dense GEMM
    dense_flops, dense_time = measure_time_and_flops(
        A_dense, B_dense, C, 'Dense', sparse=False)

    # Sparse formats: CSR, CSC, COO, DOK
    csr_flops, csr_time = measure_time_and_flops(
        A_csr, B_csr, C, 'CSR', sparse=True)
    csc_flops, csc_time = measure_time_and_flops(
        A_csc, B_csc, C, 'CSC', sparse=True)
    coo_flops, coo_time = measure_time_and_flops(
        A_coo, B_coo, C, 'COO', sparse=True)
    dok_flops, dok_time = measure_time_and_flops(
        A_dok, B_dok, C, 'DOK', sparse=True)

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
M, N, K = 1000, 1000, 1000  # Matrix sizes
density = 0.01  # 1% non-zero elements (sparse)
flops_dict, time_dict = compute_flops_gemm(M, N, K, density)

# Print results
for format_name in flops_dict:
    print(f"{format_name} format:")
    print(f"  Time taken: {time_dict[format_name]:.6f} seconds")
    print(f"  FLOPS: {flops_dict[format_name]:.2e} FLOPS")
