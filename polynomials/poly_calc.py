from numpy.polynomial import Polynomial

# Define polynomials
P = Polynomial([2, -3, 1])  # Coefficients for P(x) = 2 - 3x + x^2
Q = Polynomial([4, 0, -1])  # Coefficients for Q(x) = 4 - x^2

# Polynomial differentiation
derivative_P = P.deriv()
print("P'(x) =", derivative_P)

# Polynomial integration
integral_P = P.integ()
print("∫P(x) dx =", integral_P)
