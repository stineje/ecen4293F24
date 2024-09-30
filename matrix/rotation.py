import numpy as np

# Define the matrix to rotate (2D points)
matrix = np.array([[1, 0],
                   [0, 1],
                   [1, 1]])

# Define the rotation angle (pi/6)
theta = np.pi / 6

# Define the rotation matrix
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                            [np.sin(theta),  np.cos(theta)]])

# Rotate the matrix
rotated_matrix = np.dot(matrix, rotation_matrix)

# Print the result
print("Original matrix:\n", matrix)
print("\nRotated matrix by pi/6 radians:\n", rotated_matrix)
