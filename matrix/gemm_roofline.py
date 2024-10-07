import numpy as np
from scipy.sparse import random as sparse_random
from scipy.sparse import csr_matrix, csc_matrix
import time
import matplotlib.pyplot as plt

# Roofline plot
# James Stine and Ryan Swann

def compute_data_transferred(A, B, C, sparse=False, format_name=None):
    """
    Compute the total data transferred in bytes for GEMM operation.
    """
    if sparse:
        if format_name == 'COO':
            A_data_size = A.data.nbytes + A.row.nbytes + A.col.nbytes
            B_data_size = B.data.nbytes + B.row.nbytes + B.col.nbytes
        elif format_name == 'DOK':
            A_csr = A.tocsr()
            B_csr = B.tocsr()
            A_data_size = A_csr.data.nbytes + A_csr.indices.nbytes + A_csr.indptr.nbytes
            B_data_size = B_csr.data.nbytes + B_csr.indices.nbytes + B_csr.indptr.nbytes
        else:
            A_data_size = A.data.nbytes + A.indices.nbytes + A.indptr.nbytes
            B_data_size = B.data.nbytes + B.indices.nbytes + B.indptr.nbytes
    else:
        A_data_size = A.nbytes
        B_data_size = B.nbytes

    C_data_size = C.nbytes
    return A_data_size + B_data_size + C_data_size

def compute_flops_gemm(M, N, K, density=0.01, alpha=1.0, beta=1.0):
    """
    Compute the FLOPS and Arithmetic Intensity of GEMM for both sparse and dense matrices.
    """
    A_csr = sparse_random(M, K, density=density, format='csr', data_rvs=np.random.rand)
    B_csr = sparse_random(K, N, density=density, format='csr', data_rvs=np.random.rand)
    A_csc = csc_matrix(A_csr)
    B_csc = csc_matrix(B_csr)
    C = np.random.rand(M, N)
    A_dense = A_csr.toarray()
    B_dense = B_csr.toarray()

    def measure_time_and_flops(A, B, C, format_name, sparse=False):
        start_time = time.time()
        if sparse:
            result = alpha * A.dot(B) + beta * C
        else:
            result = alpha * np.dot(A, B) + beta * C
        end_time = time.time()

        time_taken = end_time - start_time
        flops = (2 * M * N * K) / time_taken
        data_transferred = compute_data_transferred(A, B, C, sparse=sparse, format_name=format_name)
        arithmetic_intensity = flops / data_transferred

        return flops, time_taken, data_transferred, arithmetic_intensity

    csr_flops, csr_time, csr_data, csr_ai = measure_time_and_flops(A_csr, B_csr, C, 'CSR', sparse=True)
    csc_flops, csc_time, csc_data, csc_ai = measure_time_and_flops(A_csc, B_csc, C, 'CSC', sparse=True)

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
    formats = list(flops_dict.keys())
    flops = [flops_dict[f] for f in formats]
    ai = [ai_dict[f] for f in formats]

    plt.figure(figsize=(10, 6))

    # Convert bandwidth from GB/s to bytes per second
    bandwidth_bytes_per_sec = bandwidth * 1e9

    # Plot roofline boundaries
    x = np.logspace(-2, 6, 10000000)
    plt.plot(x, np.minimum(peak_flops, bandwidth_bytes_per_sec * x), label=f'Roofline (Peak FLOPS = {peak_flops:.2e}, Bandwidth = {bandwidth} GB/s)', color='r')

    # Plot data points
    for f in formats:
        plt.scatter(ai_dict[f], flops_dict[f], label=f'{f}', s=100)

    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel('Arithmetic Intensity (FLOPs/Byte)')
    plt.ylabel('Performance (FLOPS)')
    plt.title('Roofline Plot for CSC and CSR GEMM')
    plt.legend(loc='lower right')

    plt.grid(True)
    plt.savefig('gemm_roofline.png')
    plt.show()

# Example usage:
M, N, K = 1000, 1000, 1000
density = 0.01
flops_dict, ai_dict = compute_flops_gemm(M, N, K, density)
peak_flops = 1e12
bandwidth = 100

plot_roofline(flops_dict, ai_dict, peak_flops, bandwidth)

for format_name in flops_dict:
    print(f"{format_name} format:")
    print(f"  FLOPS: {flops_dict[format_name]:.2e} FLOPS")
    print(f"  Arithmetic Intensity (AI): {ai_dict[format_name]:,.4f} FLOPs/Byte")