import math


def sine_series(x, n):
    """
    compute the series approximation of the sine function
    of x out to n terms
    """
    sineapprox = 0
    for i in range(1, n+1):
        sineapprox = sineapprox + (-1)**(i+1)*x**(2*i-1)/math.factorial(2*i-1)
    return sineapprox


x = 0.9
print('true value of sin(x)= ', math.sin(x))
n = 8
for i in range(1, 9):
    sinapp = sine_series(x, i)
    sintru = math.sin(x)
    pcterr = (sintru-sinapp)/sintru*100
    print('{0:3d}  {1:13.10g}  {2:7.3g}'.format(i, sinapp, pcterr))
