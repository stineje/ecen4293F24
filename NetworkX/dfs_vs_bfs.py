import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add edges to the graph (implicitly adds nodes as well)
edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 6), (5, 7)]
G.add_edges_from(edges)

# Function to display the graph
def draw_graph(G, title="Graph"):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=700, edge_color="gray")
    plt.title(title)
    plt.show()

# Perform Depth-First Search
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add adjacent nodes to the stack in reverse order to ensure proper DFS order
            stack.extend(reversed(list(graph.neighbors(node))))
    print()

# Perform Breadth-First Search
def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add adjacent nodes to the queue
            queue.extend(list(graph.neighbors(node)))
    print()

# Draw the graph
draw_graph(G, "Sample Graph")

# Demonstrate DFS starting from node 1
print("Depth-First Search starting from node 1:")
dfs(G, 1)

# Demonstrate BFS starting from node 1
print("Breadth-First Search starting from node 1:")
bfs(G, 1)