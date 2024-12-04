import numpy as np


def richardson_extrapolation(f, a, b, n, m):
    """
    Evaluate Richardson Extrapolation for a given function f over interval [a, b].

    Parameters:
    f  : Function to integrate
    a  : Start of interval
    b  : End of interval
    n  : Base number of intervals for trapezoidal rule
    m  : Extrapolation level

    Returns:
    Approximated integral using Richardson Extrapolation.
    """
    # Trapezoidal rule function
    def trapezoidal_rule(f, a, b, num_intervals):
        h = (b - a) / num_intervals
        x = np.linspace(a, b, num_intervals + 1)
        y = f(x)
        return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

    # Construct the extrapolation table
    T = np.zeros((m, m))
    for i in range(m):
        num_intervals = n * (2**i)
        T[i, 0] = trapezoidal_rule(f, a, b, num_intervals)
        for k in range(1, i + 1):
            T[i, k] = T[i, k - 1] + \
                (T[i, k - 1] - T[i - 1, k - 1]) / (4**k - 1)

    return T[m - 1, m - 1]


# Define the function
def f(x): return 0.2 + 25 * x - 200 * x**2 + \
    675 * x**3 - 900 * x**4 + 400 * x**5


# Parameters
a = 0
b = 0.8
n = 1  # Base intervals
m = 4  # Extrapolation level

# Evaluate
result = richardson_extrapolation(f, a, b, n, m)
print(f"Richardson Extrapolation result: {result}")
