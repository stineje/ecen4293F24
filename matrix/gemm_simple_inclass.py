import numpy as np
from scipy.sparse import random as sparse_random
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
import time


def compute_flops_sparse_gemm(M, N, K, density=0.01, alpha=1.0, beta=1.0):
    """
    Compute the FLOPS of a sparse GEMM operation for matrices of size MxK, KxN, and MxN.

    Parameters:
    M (int): Number of rows of matrix A and C.
    N (int): Number of columns of matrix B and C.
    K (int): Number of columns of matrix A and rows of matrix B.
    density (float): The density of the non-zero elements in the sparse matrix.
    alpha (float): Scalar multiplier for the product of A and B.
    beta (float): Scalar multiplier for the matrix C.

    Returns:
    flops_dict: Dictionary of FLOPS for different sparse formats (CSR, CSC, COO).
    time_dict: Dictionary of time taken for the GEMM operation in each format.
    """
    # Generate random sparse matrices A (MxK) and B (KxN)
    A_csr = sparse_random(M, K, density=density,
                          format='csr', data_rvs=np.random.rand)
    B_csr = sparse_random(K, N, density=density,
                          format='csr', data_rvs=np.random.rand)

    A_csc = csc_matrix(A_csr)
    B_csc = csc_matrix(B_csr)

    A_coo = coo_matrix(A_csr)
    B_coo = coo_matrix(B_csr)

    # Generate random dense matrix C
    C = np.random.rand(M, N)

    # Define a function to measure time and compute FLOPS
    def measure_time_and_flops(A, B, format_name):
        start_time = time.time()
        # Perform the sparse GEMM operation: C = alpha * A.dot(B) + beta * C
        result = alpha * A.dot(B) + beta * C
        end_time = time.time()
        time_taken = end_time - start_time

        # Compute the number of floating-point operations: 2 * M * N * K
        flops = (2 * M * N * K) / time_taken

        return flops, time_taken

    # Perform GEMM and calculate FLOPS for CSR format
    csr_flops, csr_time = measure_time_and_flops(A_csr, B_csr, 'CSR')

    # Perform GEMM and calculate FLOPS for CSC format
    csc_flops, csc_time = measure_time_and_flops(A_csc, B_csc, 'CSC')

    # Perform GEMM and calculate FLOPS for COO format
    coo_flops, coo_time = measure_time_and_flops(A_coo, B_coo, 'COO')

    # Store the FLOPS and times for each format in dictionaries
    flops_dict = {'CSR': csr_flops, 'CSC': csc_flops, 'COO': coo_flops}
    time_dict = {'CSR': csr_time, 'CSC': csc_time, 'COO': coo_time}

    return flops_dict, time_dict


# Example usage:
M, N, K = 1000, 1000, 1000  # Matrix sizes
density = 0.01  # 1% non-zero elements (sparse)
flops_dict, time_dict = compute_flops_sparse_gemm(M, N, K, density)

# Print results
for format_name in flops_dict:
    print(f"{format_name} format:")
    print(f"  Time taken: {time_dict[format_name]:.6f} seconds")
    print(f"  FLOPS: {flops_dict[format_name]:.2e} FLOPS")
