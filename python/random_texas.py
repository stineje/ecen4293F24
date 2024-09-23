import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_games = 10000  # Total number of games
num_experiments = 100  # Number of numerical experiments
initial_hand = ('5♣', '4♦')  # Starting hand (for reference)
win_probability = 350 / 1000  # Probability of winning based on provided stats

# Run the experiments
wins_per_experiment = []

for _ in range(num_experiments):
    wins = 0
    for _ in range(num_games):
        if np.random.rand() < win_probability:
            wins += 1
    wins_per_experiment.append(wins)

# Plotting the results as a histogram
plt.hist(wins_per_experiment, bins=10, edgecolor='black')
plt.title(
    f'Histogram of Wins in {num_experiments} Experiments \n({num_games} games per experiment with {initial_hand[0]} and {initial_hand[1]})')
plt.xlabel('Number of Wins')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('random_texas_10000.png')
plt.show()
