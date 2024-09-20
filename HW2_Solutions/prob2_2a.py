import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0.1, 0.25, 10)
# Calculate the function
y = (6*t**3-3*t-4)/8/np.sin(5*t)

# Print the results
for t_value, y_value in zip(t, y):
    print(f"y({t_value}) = {y_value}")
# Plot using matplotlib
plt.plot(t, y, c='k')
plt.grid()
plt.show()
