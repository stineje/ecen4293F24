import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import minimize

# data
ce = np.array([6.495, 6.595, 6.615, 6.635, 6.485, 6.555,
               6.665, 6.505, 6.435, 6.625, 6.715, 6.655,
               6.755, 6.625, 6.715, 6.575, 6.655, 6.605,
               6.565, 6.515, 6.555, 6.395, 6.775, 6.685])


cebar = np.mean(ce)
print('mean estimate = {0:5.3f}'.format(cebar))
cemed = np.median(ce)
print('sample median = {0:5.3f}'.format(cemed))
cemode = stats.mode(ce, axis=None)
print('sample mode = ', cemode)
cevar = np.var(ce, ddof=1)
print('sample variance = {0:7.3e}'.format(cevar))
ces = np.std(ce, ddof=1)
print('sample standard deviation = {0:7.5f}'.format(ces))

def huber_loss(mu, data, c=1.345):
    """ Huber loss function """
    diff = data - mu
    return np.sum(np.where(np.abs(diff) <= c, 0.5 * diff**2, c * (np.abs(diff) - 0.5 * c)))


res = minimize(huber_loss, np.median(ce), args=(ce,))
m_estimate = res.x[0]
print(f'M-estimate of location = {m_estimate:5.3f}')

# Histogram data
hist, bin_edges = np.histogram(ce, bins=8, range=[6.39, 6.79])
print('\nHistogram data:\n', hist)
print('\nBin boundaries:\n', bin_edges)
bin_width = bin_edges[1] - bin_edges[0]
n = len(hist)
bin_centers = np.zeros((n))
for i in range(n):
    bin_centers[i] = (bin_edges[i] + bin_edges[i + 1]) / 2

# Plot combined histogram and normal distribution curve
plt.figure(figsize=(8, 6))
plt.bar(bin_centers, hist, width=bin_width,
        color='w', edgecolor='k', label="Histogram")

# Normal distribution curve
x = np.linspace(6.39, 6.79, 100)
y = stats.norm.pdf(x, cebar, ces)
plt.plot(x, 24 * 0.05 * y, color='k', label="Normal Distribution")

# Add labels and legend
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram and Normal Distribution')
plt.legend()

# Show combined plot
plt.savefig('ch14ex.png')
plt.show()


def S(a):
    abar = np.mean(a)
    adev = a - abar
    return np.sum(adev**2)


cv = ces/cebar
print('coefficient of variation = {0:5.3f} %'.format(cv*100))
Sce = S(ce)
print('total corrected sum of squares = {0:5.3f}'.format(Sce))
MADce = stats.median_abs_deviation(ce)
print('MAD = {0:5.3e}'.format(MADce/0.6745))
