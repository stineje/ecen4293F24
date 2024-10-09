import numpy as np
import matplotlib.pyplot as plt
from book import gaussnaive

A = np.matrix('3, -0.1, -0.2; 0.1, 7.0, -0.3; 0.3, -0.2, 10.0')
b = np.matrix('7.85; -19.3; 71.4')
V = gaussnaive(A, b)
print('answer for x_1:', V[0])
print('answer for x_2:', V[1])
print('answer for x_3:', V[2])
