import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph
G = nx.DiGraph()

# Add nodes (0 to 7)
nodes = range(5)
G.add_nodes_from(nodes)

# Add edges based on the graph in the image
edges = [(0, 1), (1, 3), (0, 4), (4, 1), (2, 4), (3, 2)]
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(6, 4))
pos = nx.spring_layout(G)  # Position the nodes using a spring layout
nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=700, edge_color="gray")
plt.title("Graph Representation")
plt.show()