import numpy as np

# Define the transformation matrix
A = np.matrix([[1.5, 0.0], [0.0, 0.75]])

# Define the original vertices of the triangle
vertices = np.array([[1, 1], [2, 1], [2, 4]])

# Apply the transformation
transformed_vertices = np.dot(vertices, A.T)

# Print the transformed coordinates
print("Transformed vertices:\n", transformed_vertices)
