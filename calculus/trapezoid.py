import numpy as np


def trapezoidal_rule(f, a, b, n):
    """
    Numerically integrates a function using the trapezoidal rule.

    Parameters:
        f (function): The function to integrate.
        a (float): The start of the interval.
        b (float): The end of the interval.
        n (int): The number of subintervals.

    Returns:
        float: The numerical integral of f over [a, b].
    """
    # Step size
    h = (b - a) / n

    # Compute the x values
    x = np.linspace(a, b, n + 1)

    # Compute the y values (f(x))
    y = f(x)

    # Apply the trapezoidal rule
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

    return integral


# Example Usage
if __name__ == "__main__":
    # Define the function to integrate
    def f(x): return np.sin(x)

    # Define the integration bounds
    a, b = 0, np.pi  # Integrate sin(x) from 0 to π

    # Number of subintervals
    n = 10

    # Compute the integral
    result = trapezoidal_rule(f, a, b, n)

    print(f"Numerical integral of sin(x) from {a} to {
          b} using {n} intervals is approximately {result}")

    # Compare to exact value
    exact_value = -np.cos(b) + np.cos(a)  # Analytical integral of sin(x)
    print(f"Exact integral value: {exact_value}")
    print(f"Error: {abs(exact_value - result)}")
    print(f"Accuracy = {np.log2(abs(exact_value - result))} bits")
