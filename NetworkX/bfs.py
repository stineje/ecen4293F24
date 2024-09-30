import matplotlib.pyplot as plt
import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges to the graph
edges = [('A', 'B'), ('A', 'D'), ('B', 'D'), ('C', 'D')]
G.add_edges_from(edges)


def bfs_path(G, start, goal):
    try:
        path = nx.shortest_path(G, source=start, target=goal)
        return path
    except nx.NetworkXNoPath:
        return None


# Find path from A to C
path = bfs_path(G, 'A', 'C')

# Output the BFS path
if path:
    print(f"BFS path from A to C: {path}")
else:
    print("No path found from A to C")

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        font_weight='bold', edge_color='gray')
# Highlight the BFS path if it exists
if path:
    edge_list = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edge_list,
                           edge_color='orange', width=2)

plt.show()
