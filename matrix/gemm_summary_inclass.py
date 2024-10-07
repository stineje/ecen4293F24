import numpy as np
from scipy.sparse import random as sparse_random
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, dok_matrix
import time

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
    A_coo = coo_matrix(A_csr)
    B_coo = coo_matrix(B_csr)
    A_dok = dok_matrix(A_csr)
    B_dok = dok_matrix(B_csr)

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

    # Traditional dense GEMM
    dense_flops, dense_time, dense_data, dense_ai = measure_time_and_flops(A_dense, B_dense, C, 'Dense', sparse=False)

    # Sparse formats: CSR, CSC, COO, DOK
    csr_flops, csr_time, csr_data, csr_ai = measure_time_and_flops(A_csr, B_csr, C, 'CSR', sparse=True)
    csc_flops, csc_time, csc_data, csc_ai = measure_time_and_flops(A_csc, B_csc, C, 'CSC', sparse=True)
    coo_flops, coo_time, coo_data, coo_ai = measure_time_and_flops(A_coo, B_coo, C, 'COO', sparse=True)
    dok_flops, dok_time, dok_data, dok_ai = measure_time_and_flops(A_dok, B_dok, C, 'DOK', sparse=True)

    # Store the FLOPS, times, and AI for each format in dictionaries
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

    data_dict = {
        'Dense': dense_data,
        'CSR': csr_data,
        'CSC': csc_data,
        'COO': coo_data,
        'DOK': dok_data
    }

    ai_dict = {
        'Dense': dense_ai,
        'CSR': csr_ai,
        'CSC': csc_ai,
        'COO': coo_ai,
        'DOK': dok_ai
    }

    return flops_dict, time_dict, data_dict, ai_dict


# Example usage:
M, N, K = 1000, 1000, 1000  # Matrix sizes
density = 0.01  # 1% non-zero elements (sparse)
flops_dict, time_dict, data_dict, ai_dict = compute_flops_gemm(M, N, K, density)

# Print results with Arithmetic Intensity
for format_name in flops_dict:
    print(f"{format_name} format:")
    print(f"  Time taken: {time_dict[format_name]:.6f} seconds")
    print(f"  FLOPS: {flops_dict[format_name]:.2e} FLOPS")
    print(f"  Data transferred: {data_dict[format_name]:,.2f} Bytes")
    print(f"  Arithmetic Intensity (AI): {ai_dict[format_name]:.4f} FLOPs/Byte")