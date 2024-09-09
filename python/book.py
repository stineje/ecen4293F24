import numpy as np


def bisect(func, xl, xu, es=1.e-7, maxit=30):
    """
    Uses the bisection method to estimate a root of func(x).
    The method is iterated until the relative error from
    one iteration to the next falls below the specified
    value or until the maximum number of iterations is
    reached first.
    Input:
        func = name of the function
        xl = lower guess
        xu = upper guess
        es = relative error specification  (default 1.e-7)
        maxit = maximum number of iterations allowed (default 30)
    Output:
        xm = root estimate
        fm = function value at the root estimate
        ea = actual relative error achieved
        i+1 = number of iterations required
        or
        error message if initial guesses do not bracket solution
    """
    if func(xl)*func(xu) > 0:
        return 'initial estimates do not bracket solution'
    xmold = xl
    for i in range(maxit):
        xm = (xl+xu)/2
        ea = abs((xm-xmold)/xm)
        if ea < es:
            break
        if func(xm)*func(xl) > 0:
            xl = xm
        else:
            xu = xm
        xmold = xm
    return xm, func(xm), ea, i+1


def regfal(func, xl, xu, es=1.e-7, maxit=30):
    """
    Uses the false position method to estimate a root of func(x).
    The method is iterated until the relative error from
    one iteration to the next falls below the specified
    value or until the maximum number of iterations is
    reached first.
    Requirement: NumPy module must be imported
    Input:
        func = name of the function
        xl = lower guess
        xu = upper guess
        Ead = absolute error specification  (default 1.e-7)
        maxit = maximum number of iterations
     Output:
        xm = root estimate
        Ea = absolute error, last interval of uncertainty
        ea = actual relative error achieved
        n = number of iterations required
        or
        error message if initial guesses do not bracket solution
    """
    if func(xl)*func(xu) > 0:
        return 'initial estimates do not bracket solution'
    xmold = xl
    for i in range(maxit):
        xm = (func(xu)*xl-func(xl)*xu)/(func(xu)-func(xl))
        ea = abs((xm-xmold)/xm)
        if ea < es:
            break
        if func(xm)*func(xl) > 0:
            xl = xm
        else:
            xu = xm
        xmold = xm
    return xm, func(xm), ea, i+1
