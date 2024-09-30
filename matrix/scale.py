import numpy as np

# Define the vector to scale
vector = np.array([2, 3])

# Define a scaling matrix (scaling by 3x and 2x along x and y)
scaling_matrix = np.array([[3, 0],
                           [0, 2]])

# Scale the vector using the scaling matrix
scaled_vector = np.dot(scaling_matrix, vector)

# Output
print("Original vector:", vector)
print("Scaled vector:", scaled_vector)
