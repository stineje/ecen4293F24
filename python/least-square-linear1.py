import numpy as np
import matplotlib.pyplot as plt

# Sample data: x and y values
x = np.array([10, 20, 30, 40, 50, 60, 70, 80])
y = np.array([25, 70, 380, 550, 610, 1220, 830, 1450])

# Perform a least-squares fit: fit a line y = m*x + c
# numpy.polyfit finds the best fit for a polynomial of degree 1 (linear)
m, c = np.polyfit(x, y, 1)

# Calculate the fitted y-values
y_fit = m * x + c

# Plot the data points
plt.scatter(x, y, label='Data points')

# Plot the least-squares fit line
plt.plot(x, y_fit, color='green', label=f'Fit: y = {m:.2f}x + {c:.2f}')

# Add labels and a legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Fit')
plt.legend()

# Show the plot
plt.savefig('least-square-linear1.png')
plt.show()
