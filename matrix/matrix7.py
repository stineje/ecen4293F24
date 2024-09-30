import numpy as np
import matplotlib.pyplot as plt

A = np.matrix(' 3.6 1.2 -5.7 ; 12.9 -9.8 0.4 ; 10.6 2.9 -4.7 ')
b = np.matrix(' 12.5 ; 33.6 ; -129.1 ')
x = np.linalg.solve(A, b)
print(x)
