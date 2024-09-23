import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 10000  # Number of experiments
num_tosses = 1000  # Number of coin tosses per experiment

# Run the experiments
proportions = []
for _ in range(N):
    # 0 for tails, 1 for heads
    tosses = np.random.choice([0, 1], size=num_tosses)
    proportion_heads = np.sum(tosses) / num_tosses
    proportions.append(proportion_heads)

# Plotting the results
plt.hist(proportions, bins=10, edgecolor='black')
plt.title(f'Distribution of Heads Proportion over {N} Experiments')
plt.xlabel('Proportion of Heads')
plt.ylabel('Frequency')
plt.savefig('random_coin.png')
plt.show()
