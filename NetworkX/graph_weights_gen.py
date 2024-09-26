import random

def generate_random_graph(filename, num_nodes, num_edges):
    """ Generates a random weighted graph and writes it to a text file. """
    edges = set()

    # Ensure the graph is connected by creating a path between all nodes
    nodes = list(range(1, num_nodes + 1))
    random.shuffle(nodes)
    for i in range(num_nodes - 1):
        weight = random.randint(1, 10)  # Assign a random weight between 1 and 10
        edges.add((nodes[i], nodes[i + 1], weight))

    # Add random edges until we reach the desired number of edges
    while len(edges) < num_edges:
        u = random.randint(1, num_nodes)
        v = random.randint(1, num_nodes)
        if u != v:
            weight = random.randint(1, 10)  # Assign a random weight between 1 and 10
            edges.add((min(u, v), max(u, v), weight))  # Avoid duplicate edges

    # Write the edges with weights to the file
    with open(filename, 'w') as f:
        for u, v, weight in edges:
            f.write(f"{u} {v} {weight}\n")

# Parameters for the graph
num_nodes = 100  
num_edges = 200  
filename = "random_weighted_graph.txt"

# Generate the graph
generate_random_graph(filename, num_nodes, num_edges)

print(f"Random weighted graph with {num_nodes} nodes and {num_edges} edges has been written to {filename}.")