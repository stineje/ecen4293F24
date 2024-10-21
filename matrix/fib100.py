import numpy as np


def fibonacci_matrix(n):
    A = np.array([[1, 1],
                  [1, 0]])

    # Matrix exponentiation A^(n-1) gives us the nth Fibonacci number in the top left element
    result = np.linalg.matrix_power(A, n-1)

    # Return the top left element which is F(n)
    return result[0, 0]


# Compute the 100th Fibonacci number
fibonacci_100 = fibonacci_matrix(100)

# Format the 100th Fibonacci number with commas
fibonacci_100_formatted = f"{fibonacci_100:,}"

# Print the formatted result
print(f"The 100th Fibonacci number is: {fibonacci_100_formatted}")
