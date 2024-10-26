import numpy as np
import matplotlib.pyplot as plt

# Define polynomial coefficients
a = [1, -3.5, 2.75, 2.125, -3.875, 1.25]
# Generate roots
r = np.roots(a)

# Define a range of x values for plotting
x = np.linspace(-2, 4, 500)  # Adjust range as necessary
# Evaluate the polynomial at each x value
y = np.polyval(a, x)

# Plot the polynomial curve
plt.plot(x, y, label='Polynomial')

# Plot the roots as points on the x-axis
for root in r:
    plt.plot(root.real, 0, 'ro')  # Roots are plotted as red dots on the x-axis

# Add labels and a legend
plt.axhline(0, color='grey', lw=0.5)  # Add x-axis for reference
plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("Polynomial and its Roots")
plt.legend(["Polynomial Curve", "Roots"])
plt.grid(True)
plt.show()
