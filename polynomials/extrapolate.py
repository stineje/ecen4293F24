import numpy as np
import matplotlib.pyplot as plt

# Generate sinusoidal data within a range
x = np.linspace(0, 2 * np.pi, 10)
y = np.sin(x)  # True sinusoidal relationship

# Fit a polynomial of degree 3 to the data
coef = np.polyfit(x, y, 3)
poly = np.poly1d(coef)

# Predict within the data range and beyond
x_within = np.linspace(0, 2 * np.pi, 100)
# Extrapolate beyond the original range
x_beyond = np.linspace(0, 4 * np.pi, 200)

# Compute polynomial predictions
y_within = poly(x_within)
y_beyond = poly(x_beyond)

# Plot the data and polynomial fit
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label="Original Data (Sinusoidal)")
plt.plot(x_within, y_within, color='green', linestyle='--',
         label="Polynomial Fit (Interpolation)")
plt.plot(x_beyond, y_beyond, color='red', linestyle=':',
         label="Polynomial Fit (Extrapolation)")
plt.plot(x_beyond, np.sin(x_beyond), color='black',
         label="True Sinusoidal Relationship")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Extrapolation Hazard Example with Polynomial Fit")
plt.grid(True)
plt.show()
