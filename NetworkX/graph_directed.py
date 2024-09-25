import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
nodes = range(1, 9)  # Nodes labeled from 1 to 8
G.add_nodes_from(nodes)

# Add directed edges to the graph (connections between nodes)
edges = [
    (1, 2), (1, 3), (2, 4), (2, 5), 
    (3, 5), (4, 6), (5, 6), (5, 7),
    (6, 8), (7, 8)
]
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Position the nodes using a spring layout
nx.draw(G, pos, with_labels=True, node_color="lightgreen", font_weight="bold", node_size=2000, edge_color="black", arrows=True)
plt.title("Simple Directed Graph with 8 Vertices")
plt.show()

# Analyze the graph
print("Nodes in the graph:", G.nodes())
print("Edges in the graph:", G.edges())

# Check if the graph is strongly connected
is_strongly_connected = nx.is_strongly_connected(G)
print("Is the graph strongly connected?", is_strongly_connected)

# Find the shortest path from node 1 to node 8
shortest_path = nx.shortest_path(G, source=1, target=8)
print(f"Shortest path from node 1 to node 8: {shortest_path}")

# Calculate the in-degree and out-degree of each node
in_degrees = dict(G.in_degree())
out_degrees = dict(G.out_degree())
print("In-degree of each node:", in_degrees)
print("Out-degree of each node:", out_degrees)