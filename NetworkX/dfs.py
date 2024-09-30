import matplotlib.pyplot as plt
import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges to the graph
edges = [('A', 'B'), ('A', 'D'), ('B', 'D'), ('C', 'D')]
G.add_edges_from(edges)


def dfs_path(G, start, goal):
    try:
        # Perform DFS traversal starting from the 'start' node
        dfs_edges = list(nx.dfs_edges(G, source=start))
        # Reconstruct the path from the DFS edges
        path = reconstruct_path(dfs_edges, start, goal)
        return path
    except nx.NetworkXNoPath:
        return None


def reconstruct_path(dfs_edges, start, goal):
    """ Helper function to reconstruct path from DFS edges """
    path = [start]
    for u, v in dfs_edges:
        if v == goal:
            path.append(v)
            break
        if u == path[-1]:
            path.append(v)
    if path[-1] != goal:
        return None  # No valid path
    return path


# Find path from A to C using DFS
path = dfs_path(G, 'A', 'C')
# Output the DFS path
if path:
    print(f"DFS path from A to C: {path}")
else:
    print("No path found from A to C")
# Draw the graph and highlight the DFS path if it exists
pos = nx.spring_layout(G)
# Draw the full graph
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        font_weight='bold', edge_color='gray')
# Highlight the DFS path if it exists
if path:
    edge_list = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edge_list,
                           edge_color='orange', width=2)
plt.show()
