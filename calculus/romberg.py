import numpy as np


def romberg_integration(f, a, b, n):
    """
    Numerically integrates a function using Romberg integration.

    Parameters:
        f (function): The function to integrate.
        a (float): The start of the interval.
        b (float): The end of the interval.
        n (int): The maximum depth of the Romberg table.

    Returns:
        float: The most accurate estimate of the integral.
    """
    # Initialize Romberg table
    R = np.zeros((n, n))

    # Trapezoidal rule for the first column
    for i in range(n):
        h = (b - a) / (2 ** i)  # Step size
        R[i, 0] = 0.5 * h * (f(a) + f(b) + 2 * np.sum(f(a + j * h)
                             for j in range(1, 2**i)))

    # Richardson extrapolation
    for j in range(1, n):
        for i in range(j, n):
            R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (4**j - 1)

    # The most accurate value is in the bottom-right corner of the table
    # Return the result and the full table for inspection
    return R[n-1, n-1], R


# Example Usage
if __name__ == "__main__":
    # Define the function to integrate
    def f(x): return np.sin(x)

    # Integration bounds
    a, b = 0, np.pi  # Integrate sin(x) from 0 to π

    # Depth of Romberg table
    n = 5  # Number of levels (increases accuracy)

    # Perform Romberg integration
    integral, table = romberg_integration(f, a, b, n)

    # Print the results
    print(f"Numerical integral of sin(x) from {
          a} to {b} is approximately {integral}\n")

    # Display the Romberg table
    print("Romberg Table:")
    for i in range(n):
        print("  ".join(f"{table[i, j]:.8f}" if j <=
              i else " " * 10 for j in range(n)))

    # Compare with the exact value
    exact_value = -np.cos(b) + np.cos(a)  # Analytical integral of sin(x)
    print(f"\nExact integral value: {exact_value}")
    print(f"Error: {abs(exact_value - integral)}")
    print(f"Accuracy = {np.log2(abs(exact_value - integral))} bits")
