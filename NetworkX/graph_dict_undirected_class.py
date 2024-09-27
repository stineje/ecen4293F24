import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency dictionary
adjacency_dict = {
    'A': ['B', 'D'],
    'B': ['A', 'D'],
    'C': ['D'],
    'D': ['A', 'B', 'C']
}

# Create an empty graph
G = nx.Graph()

# Add nodes and edges based on the adjacency dictionary
for node, neighbors in adjacency_dict.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Draw the graph
plt.figure(figsize=(6, 4))
pos = nx.spring_layout(G)  # Position the nodes using a spring layout
nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=700, edge_color="gray")
plt.title("Graph Representation")
plt.show()