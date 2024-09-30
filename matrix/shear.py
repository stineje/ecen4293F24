import numpy as np
import matplotlib.pyplot as plt

# Define the grid of 2D points (let's create a simple 2x2 grid for simplicity)
points = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])

# Shear factors
sh_x = 0.5  # Shearing along the x-axis
sh_y = 0.3  # Shearing along the y-axis

# Define the shear matrices
shear_x_matrix = np.array([[1, sh_x],
                           [0, 1]])

shear_y_matrix = np.array([[1, 0],
                           [sh_y, 1]])

# Apply shear along the x-axis
sheared_points_x = np.dot(points, shear_x_matrix)

# Apply shear along the y-axis
sheared_points_y = np.dot(points, shear_y_matrix)

# Print points to the screen
print("Original Points:")
print(points)

print("\nSheared Points (along x-axis):")
print(sheared_points_x)

print("\nSheared Points (along y-axis):")
print(sheared_points_y)

# Plot original points and sheared points in separate subplots
fig, ax = plt.subplots(1, 3, figsize=(15, 5))  # 1 row, 3 columns

# --- Plot 1: Original points ---
ax[0].scatter(points[:, 0], points[:, 1],
              color='blue', label='Original points')
ax[0].axhline(0, color='black', linewidth=0.5)
ax[0].axvline(0, color='black', linewidth=0.5)
# Move legend outside the plot
ax[0].legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax[0].set_title('Original Points')
ax[0].grid(True)

# --- Plot 2: Shearing along x-axis ---
ax[1].scatter(points[:, 0], points[:, 1],
              color='blue', label='Original points')
ax[1].scatter(sheared_points_x[:, 0], sheared_points_x[:, 1],
              color='red', label='Sheared along x-axis')
# Plot connectors between original and sheared points
for i in range(len(points)):
    ax[1].plot([points[i, 0], sheared_points_x[i, 0]], [
               points[i, 1], sheared_points_x[i, 1]], 'r--', alpha=0.5)
ax[1].axhline(0, color='black', linewidth=0.5)
ax[1].axvline(0, color='black', linewidth=0.5)
# Move legend outside the plot
ax[1].legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax[1].set_title('Sheared along x-axis')
ax[1].grid(True)

# --- Plot 3: Shearing along y-axis ---
ax[2].scatter(points[:, 0], points[:, 1],
              color='blue', label='Original points')
ax[2].scatter(sheared_points_y[:, 0], sheared_points_y[:, 1],
              color='green', label='Sheared along y-axis')
# Plot connectors between original and sheared points
for i in range(len(points)):
    ax[2].plot([points[i, 0], sheared_points_y[i, 0]], [
               points[i, 1], sheared_points_y[i, 1]], 'g--', alpha=0.5)
ax[2].axhline(0, color='black', linewidth=0.5)
ax[2].axvline(0, color='black', linewidth=0.5)
# Move legend outside the plot
ax[2].legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax[2].set_title('Sheared along y-axis')
ax[2].grid(True)

# Adjust the layout
plt.tight_layout()
plt.show()
