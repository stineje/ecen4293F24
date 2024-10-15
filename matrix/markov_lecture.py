import numpy as np
import matplotlib.pyplot as plt

# slide 15, L22
# Define the initial state vector and Markov matrix
v = np.array([0.8, 0.1, 0.0, 0.1])
A = np.array([[0.6, 0.4, 0.2, 0.3],
              [0.2, 0.5, 0.1, 0.2],
              [0.15, 0.1, 0.7, 0.0],
              [0.05, 0.0, 0.0, 0.5]])


# Initialize a list to store the state vectors over time
states_over_time = [v]

# Define how many times you want to multiply the matrix by itself
num_iterations = 5

# Perform matrix multiplication
for i in range(1, num_iterations + 1):
    A_power_to_the_n = np.linalg.matrix_power(A, i)
    result = np.dot(A_power_to_the_n, v)

    print(f"Matrix after multiplication {i}:")
    print(A_power_to_the_n, "\n")
    print(f"State vector after multiplication {i}:")
    print(result, "\n")  # This prints the result state vector

    states_over_time.append(result)

# Convert the list to a numpy array for easier manipulation
states_over_time = np.array(states_over_time)

# Plot each state's probability over time
plt.figure(figsize=(10, 6))
plt.plot(states_over_time[:, 0], label='Lecture', marker='o')
plt.plot(states_over_time[:, 1], label='Surfing the Web', marker='o')
plt.plot(states_over_time[:, 2], label='Working on HW', marker='o')
plt.plot(states_over_time[:, 3], label='Texting', marker='o')

# Add labels and title
plt.xlabel('Time Steps (Minutes)')
plt.ylabel('Probability')
plt.title('Probabilities of Different Activities Over Time')
plt.legend(loc='best')

# Show the plot
plt.grid(True)
plt.show()
