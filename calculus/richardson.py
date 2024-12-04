import numpy as np


def richardson_extrapolation(f, x, h, n=2):
    """
    Computes the derivative of a function f at point x using Richardson extrapolation.

    Parameters:
        f (function): The function to differentiate.
        x (float): The point at which to evaluate the derivative.
        h (float): The initial step size.
        n (int): The order of Richardson extrapolation.

    Returns:
        float: The derivative of f at x.
    """
    # Create a 2D array for Richardson table
    R = np.zeros((n, n))

    # First column: finite differences
    for i in range(n):
        step = h / (2**i)
        R[i, 0] = (f(x + step) - f(x - step)) / (2 * step)

    # Richardson extrapolation
    for j in range(1, n):
        for i in range(j, n):
            R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (4**j - 1)

    # The most accurate value is in the bottom-right corner of the table
    return R[n-1, n-1]


# Example usage
if __name__ == "__main__":
    # Define a test function, e.g., sin(x)
    def f(x): return np.sin(x)
    x = np.pi / 4  # Point at which to differentiate
    h = 0.1        # Initial step size
    n = 4          # Order of Richardson extrapolation

    derivative = richardson_extrapolation(f, x, h, n)
    print(f"Derivative of sin(x) at x = {x} is approximately {derivative}")
