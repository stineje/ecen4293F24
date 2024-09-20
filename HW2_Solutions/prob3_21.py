import numpy as np
import matplotlib.pyplot as plt


def sinefunc(t, ybar, ydel, f, phi):
    """
      computer sine function
    """
    y = ybar + ydel * np.sin(2*np.pi*f*t-phi)
    return y


def cosinefunc(t, ybar, ydel, f, phi):
    """
      computer cosine function
    """
    y = ybar + ydel * np.cos(2*np.pi*f*t-phi)
    return y


t = np.linspace(0, 2*np.pi, 100)
# Case 1
ybar = 0
ydel = 1
phi = 0
f = 1
y1 = sinefunc(t, ybar, ydel, f, phi)
f = 1.5
y2 = sinefunc(t, ybar, ydel, f, phi)
plt.plot(t, y1, c='k', label='Base Case')
plt.plot(t, y2, c='k', ls='--', label='f = 1.5')
plt.grid()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Problem 3.21 Case 1')
plt.legend()
plt.show()

# polar plot of y1 versus t
plt.figure()
plt.polar(t, y1, c='k')
plt.title('Problem 3.21 Polar Plot of Base Case')
plt.show()

# Case 2
plt.figure()
ybar = 0
ydel = 1
phi = 0
f = 1
y1 = sinefunc(t, ybar, ydel, f, phi)
phi = np.pi/4
y2 = sinefunc(t, ybar, ydel, f, phi)
plt.plot(t, y1, c='k', label='Base Case')
plt.plot(t, y2, c='k', ls='--', label='phi = pi/4')
plt.grid()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Problem 3.21 Case 2')
plt.legend()
plt.show()

# Case 3
plt.figure()
ybar = 0
ydel = 1
phi = 0
f = 1
y1 = sinefunc(t, ybar, ydel, f, phi)
ybar = 0.5
ydel = 1.2
y2 = sinefunc(t, ybar, ydel, f, phi)
plt.plot(t, y1, c='k', label='Base Case')
plt.plot(t, y2, c='k', ls='--', label='ybar = 0.5, ydel = 1.2')
plt.grid()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Problem 3.21 Case 3')
plt.legend()
plt.show()

# Case 4
plt.figure()
ybar = 0
ydel = 1
phi = 0
f = 1
y1 = sinefunc(t, ybar, ydel, f, phi)
phi = np.pi/2
y2 = cosinefunc(t, ybar, ydel, f, phi)
plt.plot(t, y1, c='k', label='Base Case')
plt.plot(t, y2, c='k', ls='--', label='cosine, phi = pi/2')
plt.grid()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Problem 3.21 Case 4')
plt.legend()
plt.show()
