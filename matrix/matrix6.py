import numpy as np
import matplotlib.pyplot as plt

A = np.matrix([[3.6, 1.2, -5.7], [12.9, -9.8, 0.4], [10.6, 2.9, -4.7]])
Ainv = np.linalg.inv(A)
print(f"The inverse is {Ainv}")
print(f"The determinant is {np.linalg.det(A)}")
print(f"The rank is {np.linalg.matrix_rank(A)}")
print(f"The trace is {np.trace(A)}")
print(f"The transpose is {np.transpose(A)}")
