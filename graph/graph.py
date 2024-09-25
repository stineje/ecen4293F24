import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_nodes_from([4, 5, 6])

# Add edges between the nodes
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(3, 5)
G.add_edges_from([(4, 6), (5, 6)])

# Display the graph's nodes and edges
print("Nodes of the graph:", G.nodes())
print("Edges of the graph:", G.edges())

# Exploring graph properties
print("\nDegree of each node:", dict(G.degree()))
print("Is the graph connected?", nx.is_connected(G))
print("Number of connected components:", nx.number_connected_components(G))

# Shortest path between nodes
print("\nShortest path between node 1 and node 6:", nx.shortest_path(G, 1, 6))

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color="lightblue", font_weight="bold", node_size=700, edge_color="gray")
plt.title("Simple Graph Visualization")
plt.show()