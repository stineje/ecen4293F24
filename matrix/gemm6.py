import numpy as np
from scipy.sparse import random as sparse_random
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, dok_matrix
import time
import matplotlib.pyplot as plt

def compute_data_transferred(A, B, C, sparse=False, format_name=None):
    """
    Compute the total data transferred in bytes for GEMM operation.
    """
    if sparse:
        if format_name == 'COO':
            # For COO, we have data, row, and col arrays
            A_data_size = A.data.nbytes + A.row.nbytes + A.col.nbytes
            B_data_size = B.data.nbytes + B.row.nbytes + B.col.nbytes
        elif format_name == 'DOK':
            # Convert DOK to CSR for data size calculation
            A_csr = A.tocsr()
            B_csr = B.tocsr()
            A_data_size = A_csr.data.nbytes + A_csr.indices.nbytes + A_csr.indptr.nbytes
            B_data_size = B_csr.data.nbytes + B_csr.indices.nbytes + B_csr.indptr.nbytes
        else:
            # For CSR/CSC, consider the data array, indices, and indptr
            A_data_size = A.data.nbytes + A.indices.nbytes + A.indptr.nbytes
            B_data_size = B.data.nbytes + B.indices.nbytes + B.indptr.nbytes
    else:
        # For dense matrices, consider the entire arrays
        A_data_size = A.nbytes
        B_data_size = B.nbytes
    
    # C matrix is dense in all cases
    C_data_size = C.nbytes
    
    # Total data transferred is the sum of A, B, and C
    return A_data_size + B_data_size + C_data_size


def compute_flops_gemm(M, N, K, density=0.01, alpha=1.0, beta=1.0):
    """
    Compute the FLOPS and Arithmetic Intensity of GEMM for both sparse and dense matrices.
    """
    # Generate random sparse matrices A (MxK) and B (KxN)
    A_csr = sparse_random(M, K, density=density, format='csr', data_rvs=np.random.rand)
    B_csr = sparse_random(K, N, density=density, format='csr', data_rvs=np.random.rand)

    # Convert CSR matrices to other formats
    A_csc = csc_matrix(A_csr)
    B_csc = csc_matrix(B_csr)

    # Generate random dense matrix C for sparse formats and dense format
    C = np.random.rand(M, N)

    # Dense GEMM
    A_dense = A_csr.toarray()
    B_dense = B_csr.toarray()

    # Function to measure time and compute FLOPS
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

        # Compute data transferred (in bytes)
        data_transferred = compute_data_transferred(A, B, C, sparse=sparse, format_name=format_name)

        # Compute Arithmetic Intensity (FLOPs / Data Transferred)
        arithmetic_intensity = flops / data_transferred

        return flops, time_taken, data_transferred, arithmetic_intensity

    # Perform GEMM and calculate FLOPS and AI for different formats

    # Sparse formats: CSR, CSC only
    csr_flops, csr_time, csr_data, csr_ai = measure_time_and_flops(A_csr, B_csr, C, 'CSR', sparse=True)
    csc_flops, csc_time, csc_data, csc_ai = measure_time_and_flops(A_csc, B_csc, C, 'CSC', sparse=True)

    # Store the FLOPS, times, and AI for each format in dictionaries
    flops_dict = {
        'CSR': csr_flops,
        'CSC': csc_flops,
    }

    ai_dict = {
        'CSR': csr_ai,
        'CSC': csc_ai,
    }

    return flops_dict, ai_dict

def plot_roofline(flops_dict, ai_dict, peak_flops, bandwidth):
    """
    Plot the roofline model with FLOPS and Arithmetic Intensity data for CSR and CSC.
    """
    # Extract data
    formats = list(flops_dict.keys())
    flops = [flops_dict[f] for f in formats]
    ai = [ai_dict[f] for f in formats]

    # Set up the figure
    plt.figure(figsize=(10, 6))

    # Plot roofline boundaries
    x = np.logspace(-2, 2, 100)
    plt.plot(x, np.minimum(peak_flops, bandwidth * x), label=f'Roofline (Peak FLOPS = {peak_flops:.2e}, Bandwidth = {bandwidth} GB/s)', color='r')

    # Plot data points
    for f in formats:
        plt.scatter(ai_dict[f], flops_dict[f], label=f'{f}', s=100)

    # Set log scale for x and y axes
    plt.xscale('log')
    plt.yscale('log')

    # Add labels and legend
    plt.xlabel('Arithmetic Intensity (FLOPs/Byte)')
    plt.ylabel('Performance (FLOPS)')
    plt.title('Roofline Plot for CSC and CSR GEMM')
    plt.legend(loc='lower right')

    # Show the plot
    plt.grid(True)
    plt.show()

# Example usage:
M, N, K = 1000, 1000, 1000  # Matrix sizes
density = 0.01  # 1% non-zero elements (sparse)
flops_dict, ai_dict = compute_flops_gemm(M, N, K, density)

# Example parameters for roofline plot
peak_flops = 1e12  # Example peak FLOPS for the system
bandwidth = 100  # Example bandwidth in GB/s

# Plot roofline for CSR and CSC
plot_roofline(flops_dict, ai_dict, peak_flops, bandwidth)

# Print results with Arithmetic Intensity for CSR and CSC
for format_name in flops_dict:
    print(f"{format_name} format:")
    print(f"  FLOPS: {flops_dict[format_name]:.2e} FLOPS")
    print(f"  Arithmetic Intensity (AI): {ai_dict[format_name]:.4f} FLOPs/Byte")