import numpy as np
import time


def compute_flops_matrix_multiply(N):
    """
    Compute the FLOPS of matrix multiplication for two NxN matrices.

    Parameters:
    N (int): The size of the matrices (N x N).

    Returns:
    flops: The number of floating-point operations per second (FLOPS).
    """
    # Generate two random NxN matrices
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)

    # Measure the time taken for matrix multiplication
    start_time = time.time()
    C = np.dot(A, B)  # Perform matrix multiplication
    end_time = time.time()

    # Calculate time taken for multiplication
    time_taken = end_time - start_time

    # The total number of floating-point operations for matrix multiplication is 2N^3
    flops = (2 * N**3) / time_taken

    return flops, time_taken


# Example usage:
N = 1000  # Matrix size (1000x1000 matrices)
flops, time_taken = compute_flops_matrix_multiply(N)

print(
    f"Time taken for {N}x{N} matrix multiplication: {time_taken:.6f} seconds")
print(f"FLOPS: {flops:.2e} FLOPS")
