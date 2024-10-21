import numpy as np

# Define the matrix A
A = np.array([[.8, .3],
              [.2, .7]])

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Display the eigenvalues
print("Eigenvalues:\n", eigenvalues)

# Display the eigenvectors
print("\nEigenvectors:\n", eigenvectors)
