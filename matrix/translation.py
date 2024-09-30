import numpy as np

# Define the points to translate
points = np.array([[1, 1],
                   [2, 2],
                   [3, 3]])

# Define the translation vector (shifting x by 2, y by 3)
translation_vector = np.array([2, 3])

# Apply the translation
translated_points = points + translation_vector

# Output
print("Original points:\n", points)
print("Translated points:\n", translated_points)
