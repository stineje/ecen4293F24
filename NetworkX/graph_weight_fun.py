import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    """ A simple undirected weighted graph using NetworkX. """

    def __init__(self, filename):
        """ Initialize and build the graph from a file. """
        self.graph = nx.Graph()
        self.build_graph(filename)

    def build_graph(self, filename):
        """ Build the graph from the specified file. """
        with open(filename, 'r') as file:
            for line in file:
                u, v, weight = line.strip().split()
                self.graph.add_edge(u, v, weight=int(weight))

    def shortest_path(self, source, target):
        """ Find and return the shortest path from source to target based on weights. """
        try:
            path = nx.shortest_path(self.graph, source=source, target=target, weight='weight')
            return path
        except nx.NetworkXNoPath:
            print(f"No path between {source} and {target}")
            return None

    def longest_path(self):
        """ Find the longest shortest path (i.e., diameter of the graph) based on weights. """
        longest = 0
        longest_path = None
        for node in self.graph.nodes():
            for target_node in self.graph.nodes():
                if node != target_node:
                    try:
                        path_length = nx.shortest_path_length(self.graph, source=node, target=target_node, weight='weight')
                        if path_length > longest:
                            longest = path_length
                            longest_path = nx.shortest_path(self.graph, source=node, target=target_node, weight='weight')
                    except nx.NetworkXNoPath:
                        continue
        return longest, longest_path

    def draw_graph(self, path=None):
        """ Draw the graph with optional path highlighted. """
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')

        if path:
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_nodes(self.graph, pos, nodelist=path, node_color='red')
            nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, edge_color='red', width=2)

        # Draw edge labels to show weights
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)

        plt.title("Graph Visualization")
        plt.show()

# Example usage
filename = "random_weighted_graph.txt"  
graph = Graph(filename)

source = "88"  
target = "61" 

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