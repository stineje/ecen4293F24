import numpy as np


def rounder(x, n):
    """
    round x to n decimal digits
    if n is negative, round to the left of the decimal
    """
    xr = int(x*10**n+0.5)/10**n
    return xr


xtest = [477.9587, -477.9587, 0.125, 0.362945, 8192, -1357842]
ntest = [2, 2, 2, 4, -1, -3]
xrtest = np.zeros(6)
print('       x         n       rounded')
for i in range(6):
    xrtest[i] = rounder(xtest[i], ntest[i])
    print('{0:12.8g}     {1:d}  {2:12.8g}'.format(
        xtest[i], ntest[i], xrtest[i]))
