import numpy as np
import matplotlib.pyplot as plt
from book import tridiag

n = 4
e = np.zeros([n])
f = np.zeros([n])
g = np.zeros([n])
for i in range(n):
    f[i] = 2.04
    if i < n-1:
        g[i] = -1
    if i > 0:
        e[i] = -1
r = np.array(([40.8], [0.8], [0.8], [200.8]))

T = tridiag(e, f, g, r)
print('Temperatures in degC are:')
for i in range(4):
    print('       {0:6.2f}'.format(T[i]))
