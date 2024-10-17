import torch

# 1. Scalar Tensor (0-Dimensional)
scalar_tensor = torch.tensor(5)
print("Scalar Tensor:", scalar_tensor)

# 2. 1-Dimensional Tensor (Vector)
vector_tensor = torch.tensor([1, 2, 3, 4, 5])
print("1-D Tensor (Vector):", vector_tensor)

# 3. 2-Dimensional Tensor (Matrix)
matrix_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2-D Tensor (Matrix):\n", matrix_tensor)

# 4. 3-Dimensional Tensor (3x3x3 Cube)
cube_tensor = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                            [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                            [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
print("3-D Tensor (Cube):\n", cube_tensor)

# 5. Tensor of ones
ones_tensor = torch.ones(2, 3)
print("Tensor of Ones:\n", ones_tensor)

# 6. Tensor of zeros
zeros_tensor = torch.zeros(3, 4)
print("Tensor of Zeros:\n", zeros_tensor)

# 7. Tensor with random values
random_tensor = torch.rand(3, 3)
print("Tensor with Random Values:\n", random_tensor)

# 8. Tensor with a specific data type (float32)
float_tensor = torch.tensor([1.2, 2.3, 3.4], dtype=torch.float32)
print("Tensor with specific dtype (float32):", float_tensor)

# 9. Tensor for gradient tracking (requires_grad=True)
tensor_with_grad = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
print("Tensor with gradient tracking:\n", tensor_with_grad)

# 10. Reshaped Tensor (using view)
reshaped_tensor = tensor_with_grad.view(4)
print("Reshaped Tensor (1-D View):", reshaped_tensor)

# 11. GPU Tensor (if available)
if torch.cuda.is_available():
    gpu_tensor = torch.tensor([1, 2, 3], device='cuda')
    print("Tensor on GPU:", gpu_tensor)
else:
    print("No GPU available, skipping GPU tensor creation.")

# 12. Tensor with float16 (half-precision)
float16_tensor = torch.tensor([[1.2, 3.4], [5.6, 7.8]], dtype=torch.float16)
print("\nTensor with float16 (half-precision):\n", float16_tensor)

# Operations on float16 tensor
result = float16_tensor + float16_tensor
print("\nResult of addition on float16 tensor:\n", result)
