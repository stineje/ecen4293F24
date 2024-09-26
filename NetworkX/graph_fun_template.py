import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    """ Friday Fun Day: A simple undirected graph using NetworkX. """

    def __init__(self, filename):
        """ Initialize and build the graph from a file. """
        
    def build_graph(self, filename):
        """ Build the graph from the specified file. """
            
    def shortest_path(self, source, target):
        """ Find and return the shortest path from source to target. """
        try:
         
        except nx.NetworkXNoPath:
            print(f"No path between {source} and {target}")
            return None

    def longest_path(self):
        """ Find the longest shortest path (i.e., diameter of the graph). """
        longest = 0
        longest_path = None
        
        return longest, longest_path

    def draw_graph(self, path=None):
        """ Draw the graph with optional path highlighted. """
        
# Example usage
filename = "random_graph.txt"  
graph = Graph(filename)

source = "1"  
target = "42"  

# Find the shortest path and print it

# Find and print the length of the longest path

# Draw the graph and highlight the shortest path
