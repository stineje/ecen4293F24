import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes representing people
people = ["Alice", "Bob", "Carol", "Dave", "Eve"]
G.add_nodes_from(people)

# Add edges representing friendships between people
friendships = [
    ("Alice", "Bob"),
    ("Alice", "Carol"),
    ("Bob", "Dave"),
    ("Carol", "Eve"),
    ("Dave", "Eve"),
]

# Add edges to the graph
G.add_edges_from(friendships)

# Draw the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Spring layout for better visualization
nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=2000, edge_color="gray")
plt.title("Friendship Network Graph")
plt.show()

# Analyze the graph
print("Number of people (nodes):", G.number_of_nodes())
print("Number of friendships (edges):", G.number_of_edges())

# Check if the graph is connected
print("Is the friendship network fully connected?", nx.is_connected(G))

# Find the shortest path between two people
shortest_path = nx.shortest_path(G, source="Alice", target="Eve")
print(f"Shortest path between Alice and Eve: {shortest_path}")

# Centrality Measure: Degree Centrality
degree_centrality = nx.degree_centrality(G)
print("\nDegree Centrality of each person:")
for person, centrality in degree_centrality.items():
    print(f"{person}: {centrality:.2f}")