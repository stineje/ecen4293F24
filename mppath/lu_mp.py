from mpmath import mp, lu_solve, matrix

# Set precision to 50 decimal places
mp.dps = 50  # You can adjust this to the desired number of decimal places

# Define the matrix A and vector b with arbitrary precision
A = matrix([[3, -0.1, -0.2],
            [0.1, 7, -0.3],
            [0.3, -0.2, 10]])

b = matrix([7.85, -19.3, 71.4])

# Perform LU decomposition and solve for x
x = lu_solve(A, b)

# Print the solution with increased precision
print("Solution vector x with increased precision:")
for xi in x:
    print(xi)