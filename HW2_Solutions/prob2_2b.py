import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(1, 5, 10)
# Calculate the function
y = (3*t-2)/4/t - np.pi/2*t

# Print the results
for t_ans, y_ans in zip(t, y):
    print(f"y({t_ans}) = {y_ans}")
# Plot using matplotlib
plt.plot(t, y, c='k')
plt.grid()
plt.show()
