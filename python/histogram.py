# histogram_plot.py
import matplotlib.pyplot as plt

def plot_histogram(data, bins=10, title="Histogram", xlabel="Values", ylabel="Frequency"):
    """
    Plots a histogram using the provided data.

    Parameters:
    - data: list or array-like, the data to plot
    - bins: int, optional, number of bins (default is 10)
    - title: str, optional, the title of the plot
    - xlabel: str, optional, label for the x-axis
    - ylabel: str, optional, label for the y-axis
    """
    # Plot the histogram
    plt.hist(data, bins=bins, edgecolor='black')

    # Add title and labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Display the plot
    plt.savefig('histogram.png')
    plt.show()

if __name__ == "__main__":
    # Example data (replace with your own data)
    data = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    
    # Plot the histogram
    plot_histogram(data, bins=5, title="Sample Histogram", xlabel="Data Values", ylabel="Frequency")
