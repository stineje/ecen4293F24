import numpy as np


def diffex(func, dfunc, x, n):
    dftrue = dfunc(x)
    h = 1
    H = np.zeros(n)
    D = np.zeros(n)
    E = np.zeros(n)
    H[0] = h
    D[0] = (func(x+h)-func(x-h))/2/h
    E[0] = abs(dftrue-D[0])
    for i in range(1, n):
        h = h/10
        H[i] = h
        D[i] = (func(x+h)-func(x-h))/2/h
        E[i] = abs(dftrue-D[i])
    return H, D, E


def ff(x): return +np.cos(x)
def df(x): return -np.sin(x)


H, D, E = diffex(ff, df, np.pi/4, 11)

print('   step size    finite difference      true error')
for i in range(11):
    print('{0:14.10f}  {1:16.14f}   {2:16.13f}'.format(H[i], D[i], E[i]))
