from numpy.polynomial import Polynomial

# Define polynomials
P = Polynomial([2, -3, 1])  # Coefficients for P(x) = 2 - 3x + x^2
Q = Polynomial([4, 0, -1])  # Coefficients for Q(x) = 4 - x^2

# Polynomial addition and subtraction
sum_poly = P + Q
sub_poly = P - Q

print("P(x) + Q(x) =", sum_poly)
print("P(x) - Q(x) =", sub_poly)
