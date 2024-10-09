import numpy as np
import matplotlib.pyplot as plt
from book import gaussnaive

A = np.matrix('0.55,0.25,0.25 ; 0.30,0.45,0.20 ; 0.15,0.30,0.55')
b = np.matrix('4800;5800;5700')
V = gaussnaive(A, b)
print('Volume from Pit 1:', V[0])
print('Volume from Pit 2:', V[1])
print('Volume from Pit 3:', V[2])
