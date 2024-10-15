import numpy as np
import networkx as nx

# This Python computes page rank both ways using example from class
# 1.) NetworkX 2.) using a function called pagerank

# Define the updated adjacency matrix for the social graph
# Person A follows B and C, Person B follows C, and Person C follows A
M = np.array([[0, 1, 1],   # A -> B, A -> C
              [0, 0, 1],   # B -> C
              [1, 0, 0]])  # C -> A

n = M.shape[1]  # number of people (pages)
rank = np.ones(n) / n  # Initial PageRank
d = 0.85  # Damping factor


def pagerank(M, rank, d=0.85, iterations=100, tolerance=1e-6):
    # Normalize matrix (row-wise normalization)
    M = M / M.sum(axis=1, keepdims=True)
    print(M)

    for _ in range(iterations):
        prev_rank = rank.copy()
        rank = (1 - d) / n + d * M.T.dot(rank)

        # Check for convergence
        if np.linalg.norm(rank - prev_rank, 1) < tolerance:
            break
    return rank


# Calculate custom PageRank
final_rank = pagerank(M, rank)
print("Final Custom PageRank:", [f"{rank:.6f}" for rank in final_rank])

# Now, let's use NetworkX to compute PageRank
G = nx.DiGraph()

# Add edges to graph corresponding to the updated adjacency matrix M
G.add_edge(0, 1)  # A -> B
G.add_edge(0, 2)  # A -> C
G.add_edge(1, 2)  # B -> C
G.add_edge(2, 0)  # C -> A

pagerank_nx = nx.pagerank(G, alpha=d)

# Print NetworkX PageRank
print("\nNetworkX PageRank:")
for node, rank in pagerank_nx.items():
    print(f"Node {node}: {rank:.6f}")
