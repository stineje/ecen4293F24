import numpy as np
import time


def compute_flops_gemm(M, N, K, alpha=1.0, beta=1.0):
    """
    Compute the FLOPS of a GEMM operation for matrices of size MxK, KxN, and MxN.

    Parameters:
    M (int): Number of rows of matrix A and C.
    N (int): Number of columns of matrix B and C.
    K (int): Number of columns of matrix A and rows of matrix B.
    alpha (float): Scalar multiplier for the product of A and B.
    beta (float): Scalar multiplier for the matrix C.

    Returns:
    flops: The number of floating-point operations per second (FLOPS).
    time_taken: The time taken for the GEMM operation.
    """
    # Generate random matrices A, B, and C
    A = np.random.rand(M, K)
    B = np.random.rand(K, N)
    C = np.random.rand(M, N)

    # Measure time for the GEMM operation
    start_time = time.time()
    # Perform the GEMM operation: C = alpha * A * B + beta * C
    C = alpha * np.dot(A, B) + beta * C
    end_time = time.time()

    # Time taken for the operation
    time_taken = end_time - start_time

    # Calculate the number of floating-point operations for GEMM: 2 * M * N * K
    flops = (2 * M * N * K) / time_taken

    return flops, time_taken


# Example usage:
M, N, K = 1000, 1000, 1000  # Matrix sizes
flops, time_taken = compute_flops_gemm(M, N, K)

print(f"Time taken for GEMM operation: {time_taken:.6f} seconds")
print(f"FLOPS: {flops:.2e} FLOPS")
