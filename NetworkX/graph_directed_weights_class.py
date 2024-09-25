import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph
G = nx.DiGraph()

# Add nodes (0 to 7)
nodes = range(5)
G.add_nodes_from(nodes)

# Add edges based on the graph in the image
edges = [(0, 1, 3), (1, 3, 2), (0, 4, 4), (4, 1, 1), (2, 4, 1), (3, 2, 7)]
G.add_weighted_edges_from(edges)

# Print out the edges with weights
print("Edges with weights:")
for u, v, weight in G.edges(data='weight'):
    print(f"({u}, {v}, {weight})")

# Draw the graph with weights
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Use spring layout for positioning nodes
nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=2000, edge_color="gray", arrows=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Directed Graph with Weighted Edges")
plt.show()