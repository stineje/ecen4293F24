from scipy.sparse import random

def get_sparse_size(matrix):
    # Get the size of a sparse matrix in KiB
    return int((matrix.data.nbytes + matrix.indptr.nbytes + matrix.indices.nbytes) / 1024.)

def get_regular_size(matrix):
    # Get the size of a regular matrix in KiB
    return matrix.nbytes / 1024.

def calculate_flops(M, K, N):
    # Calculate the number of FLOPs for matrix multiplication
    return 2 * M * K * N  # 2 * M * K * N for matrix multiplication

# Matrix dimensions (M x K for A, K x N for B)
M, K, N = 10 ** 3, 10 ** 5, 10 ** 3

# Create a sparse matrix A (MxK) and a dense matrix B (KxN)
sparse_mat = random(M, K, format='csr')

# Get size of the sparse matrix (in KiB)
sparse_size = get_sparse_size(sparse_mat)

# Convert sparse matrix to regular matrix and get its size (in KiB)
regular_size = get_regular_size(sparse_mat.toarray())

# Calculate the number of floating-point operations (FLOPs)
flops = calculate_flops(M, K, N)

# Data transferred (size of sparse matrix + size of dense matrix)
# Assuming only the non-zero elements are transferred in sparse format
data_transferred = (sparse_mat.data.nbytes + sparse_mat.indptr.nbytes + sparse_mat.indices.nbytes + sparse_mat.toarray().nbytes) / 1024.0

# Calculate arithmetic intensity (AI)
arithmetic_intensity = flops / (data_transferred * 1024)  # data_transferred in KiB, convert to Bytes

# Print results with commas for large numbers
print(f"The size of sparse matrix is {sparse_size:,} KiB")
print(f"The size of regular matrix is {regular_size:,.2f} KiB")
print(f"Data compression ratio is {regular_size / sparse_size:,.2f}")
print(f"FLOPs: {flops:,}")
print(f"Data transferred: {data_transferred:,.2f} KiB")
print(f"Arithmetic Intensity (AI): {arithmetic_intensity:.4f} FLOPs/Byte")