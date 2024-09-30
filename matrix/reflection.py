import numpy as np

# Define the vector to reflect
vector = np.array([2, 3])

# Define the reflection matrix across the x-axis
reflection_matrix_x = np.array([[1, 0],
                                [0, -1]])

# Apply the reflection
reflected_vector_x = np.dot(reflection_matrix_x, vector)

print("Original vector:", vector)
print("Reflected vector (x-axis):", reflected_vector_x)
