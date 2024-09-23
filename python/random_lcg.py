import numpy as np
import matplotlib.pyplot as plt

# Define the LCG parameters
seed = 42          # Initial seed
a = 1664525        # Multiplier
c = 1013904223     # Increment
m = 2**32          # Modulus (Commonly used 2^32)

# Initialize the LCG state
state = seed


def lcg_next(state, a, c, m):
    """
    Generates the next random number using the LCG formula.
    """
    next_state = (a * state + c) % m
    return next_state


def lcg_generate_sequence(n, state, a, c, m):
    """
    Generates a sequence of n random numbers using LCG.
    """
    sequence = []
    for _ in range(n):
        state = lcg_next(state, a, c, m)
        sequence.append(state)
    return sequence


def lcg_generate_normalized_sequence(n, state, a, c, m):
    """
    Generates a sequence of n random numbers normalized between 0 and 1 using LCG.
    """
    sequence = []
    for _ in range(n):
        state = lcg_next(state, a, c, m)
        sequence.append(state / m)
    return sequence


# Generate a sequence of random numbers
sequence_length = 1000
normalized_sequence = lcg_generate_normalized_sequence(
    sequence_length, seed, a, c, m)

# Plot the sequence to visualize the distribution
plt.figure(figsize=(10, 6))
plt.plot(normalized_sequence, marker='o', linestyle='none')
plt.title(f'Linear Congruential Generator Sequence (n={sequence_length})')
plt.xlabel('Index')
plt.ylabel('Random Value')
plt.grid(True)
plt.savefig('random_lcg_scatter.png')
plt.show()

# Display a histogram of the generated random numbers
plt.figure(figsize=(10, 6))
plt.hist(normalized_sequence, bins=20,
         color='blue', alpha=0.7, edgecolor='black')
plt.title('Histogram of Generated Random Numbers')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('random_lcg_hist.png')
plt.show()
