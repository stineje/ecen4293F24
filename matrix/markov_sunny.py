import numpy as np
import matplotlib.pyplot as plt

# Define the transition matrix for the weather problem
A = np.array([[0.9, 0.5],
              [0.1, 0.5]])

# Define the initial state vector (today is sunny, so 100% sunny, 0% rainy)
v = np.array([1, 0])


# Initialize a list to store the state vectors over time
states_over_time = [v]

# Define how many times you want to multiply the matrix by itself
num_iterations = 5

# Perform matrix multiplication
for i in range(1, num_iterations + 1):
    A_power_to_the_n = np.linalg.matrix_power(A, i)
    result = np.dot(A_power_to_the_n, v)
    print(f"Matrix after multiplication {i}:")
    print(np.round(A_power_to_the_n, 6), "\n")
    print(f"State vector after multiplication {i}:")
    print(np.round(result, 6), "\n")

    states_over_time.append(result)

# Convert the list to a numpy array for easier manipulation
states_over_time = np.array(states_over_time)

# Plot each state's probability over time
plt.figure(figsize=(10, 6))
plt.plot(states_over_time[:, 0], label='Sunny', marker='o')
plt.plot(states_over_time[:, 1], label='Rainy', marker='o')

# Add labels and title
plt.xlabel('Time Steps (Minutes)')
plt.ylabel('Probability')
plt.title('Probabilities of Different Activities Over Time')
plt.legend(loc='best')

# Show the plot
plt.grid(True)
plt.show()
