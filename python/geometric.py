def geometric_progression(a, r, n):
    """
      Generates a geometric progression.
    """
    sequence = []
    for i in range(n):
        term = a * (r ** i)  # Compute each term
        sequence.append(term)
    return sequence


# Example usage:
a = 2  # First term
r = 3  # Common ratio
n = 10  # Number of terms

gp = geometric_progression(a, r, n)
print("Geometric Progression:", gp)
