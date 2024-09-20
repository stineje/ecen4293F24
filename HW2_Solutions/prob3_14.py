import matplotlib.pyplot as plt
import numpy as np


def piecewise(t):
    """
    evaluate 4-segment piecewise function for a single point
    """
    if t < 0:
        v = 0
    elif t <= 8:
        v = 10*t**2-5*t
    elif t <= 16:
        v = 624 - 3*t
    elif t <= 26:
        v = 36*t+12*(t-16)**2
    elif t > 26:
        v = 2136*np.exp(-0.1*(t-26))
    return v


time_points = np.linspace(-5, 50, 200)
velocity_over_time = np.array([])  # empty array to store velocity values
for time in time_points:
    velocity_over_time = np.append(velocity_over_time, [piecewise(time)])
fig, ax = plt.subplots()
ax.plot(time_points, velocity_over_time, c='m')
ax.grid()
ax.set_xlabel('t')
ax.set_ylabel('v')
ax.set_title('Problem 3.14')
plt.show()
piecewise_plot = ax
print(f"The plot is of type {type(piecewise_plot)
                             } and has values {piecewise_plot}")
