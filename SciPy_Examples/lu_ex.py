import numpy as np
from scipy.linalg import lu

# Define the matrix A and vector b
A = np.array([[3, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, 10]])

b = np.array([7.85, -19.3, 71.4])

# Perform LU decomposition
P, L, U = lu(A)

# Solve the system Ly = Pb (forward substitution)
y = np.linalg.solve(L, np.dot(P, b))

# Solve the system Ux = y (backward substitution)
x = np.linalg.solve(U, y)

# Display the solution
print("Solution vector x:")
for xi in x:
    print(f"{xi:.6f}")
    