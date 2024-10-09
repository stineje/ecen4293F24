import numpy as np


def strlinregr(x, y):
    n = len(x)
    if len(y) != n:
        return 'x and y must be of same length'
    sumx = np.sum(x)
    xbar = sumx/n
    sumy = np.sum(y)
    ybar = sumy/n
    sumsqx = 0
    sumxy = 0
    for i in range(n):
        sumsqx = sumsqx + x[i]**2
        sumxy = sumxy + x[i]*y[i]
    a1 = (n*sumxy-sumx*sumy)/(n*sumsqx-sumx**2)
    a0 = ybar - a1*xbar
    e = np.zeros((n))
    SST = 0
    SSE = 0
    for i in range(n):
        e[i] = y[i] - (a0+a1*x[i])
        SST = SST + (y[i]-ybar)**2
        SSE = SSE + e[i]**2
    SSR = SST - SSE
    Rsq = SSR/SST
    SE = np.sqrt(SSE/(n-2))
    return a0, a1, Rsq, SE


def goldmin(f, xl, xu, Ea=1.e-7, maxit=30):
    """
    use the golden-section search to find the minimum of f(x)
    input:
        f = name of the function
        xl = lower initial guess
        xu = upper initial guess
        Ea = absolute relative error criterion (default = 1.e-7)
        maxit = maximum number of iterations (default = 30)
    output:
        xopt = location of the minimum
        f(xopt) = function value at the minimum
        ea = absolute relative error achieved
        i+1 = number of iterations required
    """
    phi = (1+np.sqrt(5))/2
    d = (phi - 1)*(xu-xl)
    x1 = xl + d
    f1 = f(x1)
    x2 = xu - d
    f2 = f(x2)
    for i in range(maxit):
        xint = xu - xl
        if f1 < f2:
            xopt = x1
            xl = x2
            x2 = x1
            f2 = f1
            x1 = xl + (phi-1)*(xu-xl)
            f1 = f(x1)
        else:
            xopt = x2
            xu = x1
            x1 = x2
            f1 = f2
            x2 = xu - (phi-1)*(xu-xl)
            f2 = f(x2)
        if xopt != 0:
            ea = (2-phi)*abs(xint/xopt)
            if ea <= Ea:
                break
    return xopt, f(xopt), ea, i+1


def secant(f, x0, x1, Ea=1.e-7, maxit=30):
    """
    function to solve for the root of f(x) using the secant method
    inputs:
        f = name of f(x) function
        x0 = initial guess
        x1 = initial guess
        Ea = relative error criterion
        maxit = maximum number of iterations
    outputs:
        x2 = solution estimate for x
        f(x2) = function value at the solution estimate
        ea = relative error achieved
        i+1 = number of iterations taken
    """
    for i in range(maxit):
        x2 = x1-f(x1)/(f(x1)-f(x0))*(x1-x0)
        ea = abs((x2-x1)/x2)
        if ea < Ea:
            break
        x0 = x1
        x1 = x2
    return x2, f(x2), ea, i+1


def modsec(f, x0, delta=1.e-5, Ea=1.e-7, maxit=30):
    """
    function to solve for the root of f(x) using the secant method
    inputs:
        f = name of f(x) function
        x0 = initial guess
        delta = perturbation fraction (default 1.e-5)
        Ea = relative error criterion (default 1.e-7)
        maxit = maximum number of iterations (default 30)
    outputs:
        x2 = solution estimate for x
        f(x2) = function value at the solution estimate
        ea = relative error achieved
        i+1 = number of iterations taken
    """
    for i in range(maxit):
        x1 = x0-f(x0)/(f((1+delta)*x0)-f(x0))*delta*x0
        ea = abs((x1-x0)/x1)
        if ea < Ea:
            break
        x0 = x1
    return x1, f(x1), ea, i+1


def wegstein(g, x0, x1, Ea=1.e-7, maxit=30):
    """
    This function solves x=g(x) using the Wegstein method.
    The method is repeated until either the relative error
    falls below Ea (default 1.e-7) or reaches maxit (default 30).
    Input:
        g = name of the function for g(x)
        x0 = first initial guess for x
        x1 = second initial guess for x
        Ea = relative error threshold
        maxit = maximum number of iterations
    Output:
        x2 = solution estimate
        ea = relative error
        i+1 = number of iterations
    """
    for i in range(maxit):
        x2 = (x1*g(x0)-x0*g(x1))/(x1-x0-g(x1)+g(x0))
        ea = abs((x1-x0)/x1)
        if ea < Ea:
            break
        x0 = x1
        x1 = x2
    return x2, ea, i+1


def newtraph(f, fp, x0, Ea=1.e-7, maxit=30):
    """
    This function solves f(x)=0 using the Newton-Raphson method.
    The method is repeated until either the relative error
    falls below Ea (default 1.e-7) or reaches maxit (default 30).
    Input:
        f = name of the function for f(x)
        fp = name of the function for f'(x)
        x0 = initial guess for x
        Ea = relative error threshold
        maxit = maximum number of iterations
    Output:
        x1 = solution estimate
        f(x1) = equation error at solution estimate
        ea = relative error
        i+1 = number of iterations
    """
    for i in range(maxit):
        x1 = x0 - f(x0)/fp(x0)
        ea = abs((x1-x0)/x1)
        if ea < Ea:
            break
        x0 = x1
    return x1, f(x1), ea, i+1


def brentsimp(f, xl, xu):
    eps = np.finfo(float).eps
    a = xl
    b = xu
    fa = f(a)
    fb = f(b)
    c = a
    fc = fa
    d = b - c
    e = d
    while True:
        if fb == 0:
            break
        if np.sign(fa) == np.sign(fb):  # rearrange points as req'd
            a = c
            fa = fc
            d = b - c
            e = d
        if abs(fa) < abs(fb):
            c = b
            b = a
            a = c
            fc = fb
            fb = fa
            fa = fc
        m = (a-b)/2  # termination test and possible exit
        tol = 2 * eps * max(abs(b), 1)
        if abs(m) < tol or fb == 0:
            break
        # choose open methods or bisection
        if abs(e) >= tol and abs(fc) > abs(fb):
            s = fb/fc
            if a == c:
                # secant method here
                p = 2*m*s
                q = 1 - s
            else:
                # inverse quadratic interpolation here
                q = fc/fa
                r = fb/fa
                p = s * (2*m*q*(q-r)-(b-c)*(r-1))
                q = (q-1)*(r-1)*(s-1)
            if p > 0:
                q = -q
            else:
                p = -p
            if 2*p < 3*m*q - abs(tol*q) and p < abs(0.5*e*q):
                e = d
                d = p/q
            else:
                d = m
                e = m
        else:
            # bisection here
            d = m
            e = m
        c = b
        fc = fb
        if abs(d) > tol:
            b = b + d
        else:
            b = b - np.sign(b-a)*tol
        fb = f(b)
    return b


def fixpt(g, x0, Ea=1.e-7, maxit=30):
    """
    This function solves x=g(x) using fixed-point iteration.
    The method is repeated until either the relative error
    falls below Ea (default 1.e-7) or reaches maxit (default 30).
    Input:
        g = name of the function for g(x)
        x0 = initial guess for x
        Ea = relative error threshold
        maxit = maximum number of iterations
    Output:
        x1 = solution estimate
        ea = relative error
        i+1 = number of iterations
    """
    for i in range(maxit):
        x1 = g(x0)
        ea = abs((x1-x0)/x1)
        if ea < Ea:
            break
        x0 = x1
    return x1, ea, i+1


def incsearch(func, xmin, xmax, ns=50):
    """
    incsearch: incremental search locator
        incsearch(func,xmin,xmax,ns)
        finds brackets of x that contain sign changes in
        a function of x on an interval
    input: 
        func = name of the function
        xmin, xmax = endpoints of the interval
        ns = number of subintervals, default value = 50
    output:  a tuple containing
        nb = number of bracket pairs found
        xb = list of bracket pair values
        or returns "no brackets found"
    """
    x = np.linspace(xmin, xmax, ns)  # create array of x values
    f = []  # build array of corresponding function values
    for k in range(ns-1):
        f.append(func(x[k]))
    nb = 0
    xb = []
    for k in range(ns-2):  # check adjacent pairs of function values
        if func(x[k])*func(x[k+1]) < 0:  # for sign change
            nb = nb + 1  # increment the bracket counter
            xb.append((x[k], x[k+1]))  # save the bracketing pair
    if nb == 0:
        return 'no brackets found'
    else:
        return nb, xb


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


def gaussnaive(A, b):
    """
    gaussnaive: naive Gauss elimination
    input:
    A = coefficient matrix
    b = constant vector
    output:
    x = solution vector
    """
    (n, m) = A.shape
    # n = nm[0]
    # m = nm[1]
    if n != m:
        return 'Coefficient matrix A must be square'
    nb = n+1
    # build augmented matrix
    Aug = np.hstack((A, b))
    # forward elimination
    for k in range(n-1):
        for i in range(k+1, n):
            factor = Aug[i, k]/Aug[k, k]
            Aug[i, k:nb] = Aug[i, k:nb]-factor*Aug[k, k:nb]
    # back substitution
    x = np.zeros([n, 1])  # create empty x array
    x = np.matrix(x)  # convert to matrix type
    x[n-1] = Aug[n-1, nb-1]/Aug[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = (Aug[i, nb-1]-Aug[i, i+1:n]*x[i+1:n, 0])/Aug[i, i]
    return x


def gausspivot(A, b):
    """
    gausspivot: Gauss elimination with partial pivoting
    input:
    A = coefficient matrix
    b = constant vector
    output:
    x = solution vector
    """
    (n, m) = A.shape
    if n != m:
        return 'Coefficient matrix A must be square'
    nb = n+1
    # build augmented matrix
    Aug = np.hstack((A, b))
    # forward elimination
    for k in range(n-1):

        # partial pivoting
        imax = maxrow(Aug[k:n, k])
        ipr = imax + k
        if ipr != k:  # no row swap if pivot is max
            for j in range(k, nb):  # swap rows k and ipr
                temp = Aug[k, j]
                Aug[k, j] = Aug[ipr, j]
                Aug[ipr, j] = temp

        for i in range(k+1, n):
            factor = Aug[i, k]/Aug[k, k]
            Aug[i, k:nb] = Aug[i, k:nb]-factor*Aug[k, k:nb]
    # back substitution
    x = np.zeros([n, 1])  # create empty x array
    x = np.matrix(x)  # convert to matrix type
    x[n-1] = Aug[n-1, nb-1]/Aug[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = (Aug[i, nb-1]-Aug[i, i+1:n]*x[i+1:n, 0])/Aug[i, i]
    return x


def maxrow(avec):
    # function to determine the row index of the
    # maximum value in a vector
    maxrowind = 0
    n = len(avec)
    amax = abs(avec[0])
    for i in range(1, n):
        if abs(avec[i]) > amax:
            amax = avec[i]
            maxrowind = i
    return maxrowind


def tridiag(e, f, g, r):
    """
    tridiag: solves a set of n linear algebraic equations
             with a tridiagonal-banded coefficient matris
    input:
    e = subdiagonal vector of length n, first element = 0
    f = diagonal vector of length n
    g = superdiagonal vector of length n, last element = 0
    r = constant vector of length n
    output:
    x = solution vector of length n
    """
    n = len(f)
    # forward elimination
    x = np.zeros([n])
    for k in range(1, n):
        factor = e[k]/f[k-1]
        f[k] = f[k] - factor*g[k-1]
        r[k] = r[k] - factor*r[k-1]
    # back substitution
    x[n-1] = r[n-1]/f[n-1]
    for k in range(n-2, -1, -1):
        x[k] = (r[k] - g[k]*x[k+1])/f[k]
    return x
