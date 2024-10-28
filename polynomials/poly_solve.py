import numpy as np

A = np.matrix(
    '90000.0, 300.0, 1.0; 160000.0, 400.0, 1.0; 250000.0, 500.0, 1.0')
b = np.matrix('0.616; 0.525; 0.457')
p = np.linalg.solve(A, b)
print(p)
print(('{0:7.5g}'.format(np.linalg.cond(A))))
