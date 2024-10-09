import numpy as np
import time


def print_time_in_engineering_units(time_in_seconds, label):
    """ print the time in engineering notation. """
    exponent = int(np.floor(np.log10(time_in_seconds) / 3) * 3)
    mantissa = time_in_seconds / (10 ** exponent)
    print(f"{label}: {mantissa:.3f}e{exponent:+03d} seconds")


def generate_random_square_matrix(N):
    # Generate a random square matrix of size N x N with values between 0 and 1
    matrix = np.random.rand(N, N)
    return matrix


# Example usage:
N = 100000  # Set the size of the matrix
matrix = generate_random_square_matrix(N)

# print(f"Random {N}x{N} matrix:")
# print(matrix)
start_time = time.time()
AT = np.transpose(matrix)
end_time = time.time()
print_time_in_engineering_units(
    end_time - start_time, "Time taken to build graph")
