import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes representing OSU coaching staff categories
categories = ["Offensive Staff", "Defensive Staff", "Special & Strength"]
G.add_nodes_from(categories)

# Add nodes representing individual coaches
offensive_staff = ["Mike Gundy", "Charlie Dickey", "Kasey Dunn", "Jason McEndoo", "Tim Rattay", "John Wozniak"]
defensive_staff = ["Joe Bob Clements", "Tim Duffie", "Bryan Nardo", "Paul Randolph"]
special_and_strength = ["Sean Snyder", "Rob Glass"]

# Add edges connecting coaches to their respective category nodes
for coach in offensive_staff:
    G.add_edge(coach, "Offensive Staff")
    
for coach in defensive_staff:
    G.add_edge(coach, "Defensive Staff")
    
for coach in special_and_strength:
    G.add_edge(coach, "Special & Strength")

# Draw the graph
plt.figure(figsize=(10, 8))

# Positioning: Center the category nodes, with the coaches surrounding them
pos = nx.spring_layout(G, k=0.5)  # Spring layout for better visualization

# Draw nodes
nx.draw_networkx_nodes(G, pos, nodelist=categories, node_color="orange", node_size=2500, label=True)
nx.draw_networkx_nodes(G, pos, nodelist=offensive_staff + defensive_staff + special_and_strength, 
                       node_color="lightblue", node_size=2000)

# Draw edges
nx.draw_networkx_edges(G, pos, width=2, edge_color="gray")

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

# Set plot title and show the graph
plt.title("OSU Football Coaching Staff Organized by Categories")
plt.axis('off')  # Hide axes
plt.show()

# Analyze the graph
print("Number of nodes (categories + coaches):", G.number_of_nodes())
print("Number of edges (relationships):", G.number_of_edges())

# Centrality Measure: Degree Centrality
degree_centrality = nx.degree_centrality(G)
print("\nDegree Centrality of each node:")
for node, centrality in degree_centrality.items():
    print(f"{node}: {centrality:.2f}")
