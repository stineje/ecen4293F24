import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph
G = nx.Graph()

# Add nodes to the graph
nodes = range(1, 9)  # Nodes labeled from 1 to 8
G.add_nodes_from(nodes)

# Add edges to the graph (connections between nodes)
edges = [
    (1, 2), (1, 3), (2, 4), (2, 5), 
    (3, 5), (4, 6), (5, 6), (5, 7),
    (6, 8), (7, 8)
]
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Position the nodes using a spring layout
nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=2000, edge_color="gray")
plt.title("Simple Undirected Graph with 8 Vertices")
plt.show()

# Analyze the graph
print("Nodes in the graph:", G.nodes())
print("Edges in the graph:", G.edges())

# Check if the graph is connected
is_connected = nx.is_connected(G)
print("Is the graph connected?", is_connected)

# Find the shortest path between two nodes
shortest_path = nx.shortest_path(G, source=1, target=8)
print(f"Shortest path from node 1 to node 8: {shortest_path}")

# Calculate the degree of each node (number of connections)
degree = dict(G.degree())
print("Degree of each node:", degree)