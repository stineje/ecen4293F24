import torch

print("Using torch", torch.__version__)
# Define two matrices (A and B)
A = torch.tensor([[1, 2],
                  [3, 4]])

B = torch.tensor([[5, 6],
                  [7, 8]])

# Perform matrix multiplication
result = torch.matmul(A, B)

# Print the result
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nResult of A * B (Matrix Multiplication):")
print(result)
