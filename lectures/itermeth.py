import math
import numpy as np


def itermeth(x, es=1e-4, maxit=50):
    """
    Maclaurin series expansion of the exponential function
    requires math module
    input:
        x = value at which the series is evaluated
        es = stopping criterion (default = 1e-4)
        maxit = maximum number of iterations (default=10)
    output:
        fx = estimated function value
        ea = approximate relative error (%)
        iter = number of iterations
    """
    # initialization
    iter = 1
    sol = 1
    ea = 100
    # iterative calculation
    while True:
        solold = sol
        sol = sol + x**iter / math.factorial(iter)
        iter = iter + 1
        if sol != 0:
            ea = abs((sol-solold)/sol)*100
        if ea < es or iter == maxit:
            break
    fx = sol
    return fx, ea, iter


# Packing of result
approxval, ea, iter = itermeth(0.5, 1e-6, 100)
print(f"approx: {approxval} error {ea} iterations {iter}")
