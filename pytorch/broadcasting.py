import torch

# 2D tensor (shape: 3x3)
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 1D tensor (shape: 1x3)
B = torch.tensor([10, 20, 30])

# Broadcasting addition
C = A + B

print("A:\n", A)
print("B:\n", B)
print("A + B:\n", C)
