def arithmetic_progression(a, d, n):
    """
      Generates an arithmetic progression.
    """
    sequence = []
    for i in range(n):
        term = a + i * d  # Compute each term
        sequence.append(term)
    return sequence


# Example usage:
a = 2  # First term
d = 5  # Common difference
n = 10  # Number of terms

ap = arithmetic_progression(a, d, n)
print("Arithmetic Progression:", ap)
