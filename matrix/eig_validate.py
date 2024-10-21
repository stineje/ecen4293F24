import numpy as np

# Define the matrix A
A = np.array([[.8, .3],
              [.2, .7]])

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
# Verify the eigenvalue-eigenvector relationship for the first eigenvalue and eigenvector
v = eigenvectors[:, 0]  # First eigenvector
lambda_1 = eigenvalues[0]  # First eigenvalue

# Compute A * v
Av = np.dot(A, v)

# Compute lambda * v
lambda_v = lambda_1 * v

# Compute the trace of the matrix
trace_value = np.trace(A)

print("\nA * v:\n", Av)
print("\nlambda * v:\n", lambda_v)
print("Trace of the matrix A:", trace_value)
