from numpy.polynomial import Polynomial

# Define two polynomials, e.g., P(x) = x^2 - 3x + 2 and Q(x) = -x^2 + 4
P = Polynomial([2, -3, 1])  # Coefficients for P(x) = 2 - 3x + x^2
Q = Polynomial([4, 0, -1])  # Coefficients for Q(x) = 4 - x^2

# 1. Polynomial Addition: P(x) + Q(x)
sum_poly = P + Q
print("P(x) + Q(x) =", sum_poly)

# 2. Polynomial Subtraction: P(x) - Q(x)
sub_poly = P - Q
print("P(x) - Q(x) =", sub_poly)

# 3. Polynomial Multiplication: P(x) * Q(x)
mul_poly = P * Q
print("P(x) * Q(x) =", mul_poly)

# 4. Polynomial Differentiation (Derivative): P'(x)
derivative_P = P.deriv()
print("P'(x) =", derivative_P)

# 5. Polynomial Integration (Indefinite Integral): ∫P(x)dx
integral_P = P.integ()
print("∫P(x) dx =", integral_P)
