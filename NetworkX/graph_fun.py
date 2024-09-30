import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time

class Graph:
    """ Friday Fun Day: A simple undirected graph using NetworkX. """

    def __init__(self, filename):
        """ Initialize and build the graph from a file. """
        self.graph = nx.Graph()
        start_time = time.time()
        self.build_graph(filename)
        end_time = time.time()
        self.print_time_in_engineering_units(end_time - start_time, "Time taken to build graph")

    def build_graph(self, filename):
        """ Build the graph from the specified file. """
        with open(filename, 'r') as file:
            for line in file:
                # print(f"Reading line: {line.strip()}")
                u, v = line.strip().split()
                self.graph.add_edge(u, v)

    def shortest_path(self, source, target):
        """ 
            Find and return the shortest path from source to target. 
            path : Uses NetworkX shortest_path to find shortest_path, 
            if path is none, it should print out such. 
        """
        try:
            start_time = time.time()
            path = nx.shortest_path(self.graph, source=source, target=target)
            end_time = time.time()
            self.print_time_in_engineering_units(end_time - start_time, "Time taken to find shortest path")
            return path
        except nx.NetworkXNoPath:
            print(f"No path between {source} and {target}")
            return None

    def longest_path(self):
        """
            Find and return the shortest path from source to target. 
            path : Uses NetworkX shortest_path_length to find the longest path,
            once identified, use the shortest_path method to indicate the path.
            if path is none, it should print out such. 
        """
        longest = 0
        longest_path = None
        start_time = time.time()
        for node in self.graph.nodes():
            for target_node in self.graph.nodes():
                if node != target_node:
                    try:
                        path_length = nx.shortest_path_length(self.graph, source=node, target=target_node)
                        if path_length > longest:
                            longest = path_length
                            longest_path = nx.shortest_path(self.graph, source=node, target=target_node)
                    except nx.NetworkXNoPath:
                        continue
        end_time = time.time()
        self.print_time_in_engineering_units(end_time - start_time, "Time taken to find longest path")
        return longest, longest_path

    def draw_graph(self, path=None):
        """ Draw the graph with optional path highlighted. """
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')

        if path:
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_nodes(self.graph, pos, nodelist=path, node_color='red')
            nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, edge_color='red', width=2)

        plt.title("Graph Visualization")
        plt.show()

    def print_time_in_engineering_units(self, time_in_seconds, label):
        """ print the time in engineering notation. """
        exponent = int(np.floor(np.log10(time_in_seconds) / 3) * 3)
        mantissa = time_in_seconds / (10 ** exponent)
        print(f"{label}: {mantissa:.3f}e{exponent:+03d} seconds")

# Example usage
filename = "random_graph.txt"  
graph = Graph(filename)

source = "4"  
target = "37"  

# Find the shortest path and print it
path = graph.shortest_path(source, target)
if path:
    print(f"Shortest path from {source} to {target}: {path}")

# Find and print the length of the longest path
longest_path_length, longest_path = graph.longest_path()
print(f"Length of the longest path in the graph: {longest_path_length}")
print(f"Longest path in the graph: {longest_path}")

# Draw the graph and highlight the shortest path
graph.draw_graph(path)