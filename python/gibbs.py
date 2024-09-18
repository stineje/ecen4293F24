import numpy as np
import matplotlib.pyplot as plt

# Create a square wave function
def square_wave(x):
    return np.where(np.sin(x) >= 0, 1, -1)

# Fourier series approximation of a square wave
def fourier_series_square_wave(x, n_terms):
    result = np.zeros_like(x)
    for n in range(1, n_terms + 1, 2):  # Only odd terms (n = 1, 3, 5, ...)
        result += (4 / (np.pi * n)) * np.sin(n * x)
    return result

# Plot the square wave and its Fourier approximation
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
square_wave_values = square_wave(x)

plt.figure(figsize=(10, 6))
plt.plot(x, square_wave_values, label='Square Wave', color='black', linewidth=2)

# Plot Fourier approximations with different numbers of terms
for n_terms in [1, 3, 5, 11, 51]:
    y_approx = fourier_series_square_wave(x, n_terms)
    plt.plot(x, y_approx, label=f'{n_terms} terms')

plt.title('Gibbs Phenomenon - Fourier Series Approximation of a Square Wave')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.savefig('gibbs.png')
plt.show()
