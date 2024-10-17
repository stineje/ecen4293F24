import torch

# Check if bfloat16 is available on the current device (usually requires specific GPUs or TPUs)
if torch.cuda.is_available():
    device = torch.device('cuda')
    print("CUDA enabled")
else:
    device = torch.device('cpu')
    print("CPU enabled")

# Create a bfloat16 tensor
bfloat16_tensor = torch.tensor(
    [[1.5, 2.5], [3.5, 4.5]], dtype=torch.bfloat16, device=device)
print("bfloat16 Tensor:\n", bfloat16_tensor)

# Perform an operation (e.g., addition) on the bfloat16 tensor
result = bfloat16_tensor + bfloat16_tensor
print("\nResult of addition on bfloat16 tensor:\n", result)

# Check the data type of the result
print("\nData type of the result:", result.dtype)
