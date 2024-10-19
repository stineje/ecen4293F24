import numpy as np

# Define two large matrices A and B (8x8 in this case)
A = np.random.randint(0, 10, (8, 8))
B = np.random.randint(0, 10, (8, 8))

# Define the size of the blocks (e.g., 4x4)
block_size = 2

# Function to perform block matrix multiplication


def block_multiply(A, B, block_size):
    n = A.shape[0]
    C = np.zeros((n, n), dtype=int)

    # Split matrices into blocks and perform multiplication
    for i in range(0, n, block_size):
        for j in range(0, n, block_size):
            for k in range(0, n, block_size):
                # Extract the blocks from matrices A and B
                A_block = A[i:i+block_size, k:k+block_size]
                B_block = B[k:k+block_size, j:j+block_size]

                # Perform the block multiplication and accumulate the result in C
                C[i:i+block_size, j:j+block_size] += np.dot(A_block, B_block)

    return C


# Perform block matrix multiplication
C = block_multiply(A, B, block_size)

# Print the original matrices and the result
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nResult of Block Matrix Multiplication (A * B):")
print(C)

# Verify by directly multiplying the full matrices
C_direct = np.dot(A, B)
print("\nDirect Multiplication Result (A * B):")
print(C_direct)

# Check if the block multiplication result matches the direct multiplication result
print("\nDoes Block Multiplication match Direct Multiplication?")
print(np.array_equal(C, C_direct))
