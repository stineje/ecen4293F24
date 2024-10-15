import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# PR for slide 30, L22 (last node adjusted to 1/6)
v = np.array([0.1, 0.2, 0.1, 0.3, 0.1, 0.2])
A = np.array([[0, 0, 0, 1.0, 0, 1/6],
              [1, 0, 0, 0, 0, 1/6],
              [0, 1, 0, 0, 0, 1/6],
              [0, 1, 1, 0, 0, 1/6],
              [0, 0, 1, 0, 0, 1/6],
              [1, 0, 1, 0, 1.0, 1/6]])

# Compute the sum of each column
col_sum = A.sum(axis=0)
# Divide each element in A by the corresponding column sum
# Avoid division by zero by handling cases where column sum is zero
A = np.divide(A, col_sum, where=col_sum != 0)

# Initialize a list to store the state vectors over time
states_over_time = [v]

# Define how many iterations
num_iterations = 15

# Perform iterative matrix multiplication (Markov process)
for i in range(1, num_iterations + 1):
    # Multiply the previous state by A
    A_power_to_the_n = np.linalg.matrix_power(A, i)
    result = np.dot(A, states_over_time[-1])
    print(f"Matrix after multiplication {i}:")
    print(A_power_to_the_n, "\n")
    print(f"State vector after iteration {i}:")
    # This prints the result state vector rounded to 6 decimal places
    print(np.round(result, 6), "\n")
    states_over_time.append(result)

# Convert the list to a numpy array for easier manipulation
states_over_time = np.array(states_over_time)

# Plot each state's probability over time
plt.figure(figsize=(10, 6))
plt.plot(states_over_time[:, 0], label='Web 0', marker='o')
plt.plot(states_over_time[:, 1], label='Web 1', marker='o')
plt.plot(states_over_time[:, 2], label='Web 2', marker='o')
plt.plot(states_over_time[:, 3], label='Web 3', marker='o')
plt.plot(states_over_time[:, 4], label='Web 4', marker='o')
plt.plot(states_over_time[:, 5], label='Web 5', marker='o')

# Add labels and title
plt.xlabel('Time Steps')
plt.ylabel('Probability')
plt.title('Probabilities of Different Activities Over Time')
plt.legend(loc='best')

# Show the plot
plt.grid(True)
plt.show()

# Create a directed graph using NetworkX from the adjacency matrix (normalized)
G = nx.from_numpy_array(A, create_using=nx.DiGraph)
print(A)

# Compute PageRank using NetworkX's built-in function
pagerank = nx.pagerank(G, alpha=0.85)

# Print the PageRank results
print("PageRank Results (unordered):")
for node, rank in pagerank.items():
    print(f"Node {node}: {rank:.6f}")

# Ensure PageRank results are printed in node order (0 to 5)
print("\nPageRank Results (ordered by node):")
for node in sorted(pagerank.keys()):
    print(f"Node {node}: {pagerank[node]:.6f}")

# Explicitly compare PageRank and plotted probabilities in the same order
for i in range(len(v)):
    print(f"State vector (Plotted) for Node {
          i}: {states_over_time[-1][i]:.6f}")
    # Use integer indexing here
    print(f"PageRank for Node {i}: {pagerank[i]:.6f}")
