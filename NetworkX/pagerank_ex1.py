import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# PR for slide 27, L22
G = nx.DiGraph()

# Add edges to the graph
edges = [("0", "1"), ("1", "2"), ("1", "3"), ("2", "3"), ("3", "0"),
         ("2", "4"), ("4", "5"), ("2", "5"), ("0", "5"), ("5", "0")]
G.add_edges_from(edges)

# Parameters for PageRank
alpha = 0.85  # Damping factor Brin/Page
num_iterations = 15  # Number of iterations to simulate

# Get the number of nodes and initialize the PageRank values
nodes = list(G.nodes())
n = len(nodes)
pagerank_scores = np.array([1 / n] * n)  # Uniform initial distribution
pagerank_scores_over_time = [pagerank_scores.copy()]

# Adjacency matrix (transition matrix)
adj_matrix = nx.adjacency_matrix(G).todense()
adj_matrix = np.array(adj_matrix, dtype=float)

# Normalize the adjacency matrix to create the transition matrix (probabilities)
for i in range(n):
    if adj_matrix[i].sum() > 0:
        adj_matrix[i] /= adj_matrix[i].sum()
print(adj_matrix)

# Perform PageRank iteration over time (slide 20, L22)
for _ in range(num_iterations):
    pagerank_scores = (1 - alpha) / n + alpha * \
        adj_matrix.T.dot(pagerank_scores)
    pagerank_scores_over_time.append(pagerank_scores.copy())

# Convert results to a NumPy array for easier plotting
pagerank_scores_over_time = np.array(pagerank_scores_over_time)

# Plot the PageRank scores evolution over time
plt.figure(figsize=(10, 6))
for i, node in enumerate(nodes):
    plt.plot(pagerank_scores_over_time[:, i], label=f"Node {node}", marker='o')

plt.xlabel("Time Step (Iteration)")
plt.ylabel("PageRank Score")
plt.title("PageRank Evolution Over Time for Each Node")
plt.legend(loc="best")
plt.grid(True)
plt.show()

# Print the final PageRank scores
print("Final PageRank Scores after iterations:")
final_pagerank = pagerank_scores_over_time[-1]
for i, node in enumerate(nodes):
    print(f"Node {node}: {final_pagerank[i]:.6f}")
