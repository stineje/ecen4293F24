import torch

# Creating tensors
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

# Perform basic operations
addition = a + b
multiplication = a * b
matrix_multiplication = torch.matmul(a, b)

# Display results
print("Tensor A:\n", a)
print("Tensor B:\n", b)
print("Addition (A + B):\n", addition)
print("Element-wise Multiplication (A * B):\n", multiplication)
print("Matrix Multiplication (A @ B):\n", matrix_multiplication)
