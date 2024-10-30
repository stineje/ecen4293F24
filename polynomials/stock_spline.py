import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Simulated daily stock prices over a week (5 trading days)
days = np.array([0, 1, 2, 3, 4])  # Days of the week (e.g., Monday to Friday)
prices = np.array([100, 102, 98, 105, 107])  # Stock prices on each day

# Create a cubic spline to interpolate the stock price data
spline = CubicSpline(days, prices)

# Generate a dense range of values for a smooth curve
days_dense = np.linspace(0, 4, 100)  # Fractional days for smooth plotting
prices_spline = spline(days_dense)  # Evaluate the spline at each point

# Plot the original stock price data points and the interpolated spline
plt.figure(figsize=(10, 5))
plt.plot(days_dense, prices_spline,
         label="Cubic Spline Interpolation", color="blue")
plt.scatter(days, prices, color="red",
            label="Stock Price Data Points", zorder=5)
plt.xlabel("Days")
plt.ylabel("Stock Price (USD)")
plt.legend()
plt.title("Stock Price Interpolation Using Cubic Spline")
plt.grid(True)
plt.show()
