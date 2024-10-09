import numpy as np
import matplotlib.pyplot as plt
from book import gausspivot, gaussnaive

A = np.matrix('1.0, 2.0, 3.0; 2.0, 4.0001, 6.0; 3.0, 6.0, 9.0')
b = np.matrix('1; 2; 3')

x1 = gausspivot(A, b)
x2 = gaussnaive(A, b)
print(x1)
print(x2)
