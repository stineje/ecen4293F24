from numpy.polynomial import Polynomial

# Define polynomials
P = Polynomial([2, -3, 1])  # Coefficients for P(x) = 2 - 3x + x^2
Q = Polynomial([4, 0, -1])  # Coefficients for Q(x) = 4 - x^2

# Evaluate P(x) at x = 1
x_val = 1
P_val = P(x_val)
print(f"P({x_val}) =", P_val)
