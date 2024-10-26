from numpy.polynomial import Polynomial

# Define polynomials
P = Polynomial([2, -3, 1])  # Coefficients for P(x) = 2 - 3x + x^2
Q = Polynomial([4, 0, -1])  # Coefficients for Q(x) = 4 - x^2

# Polynomial multiplication
mul_poly = P * Q
print("P(x) * Q(x) =", mul_poly)
