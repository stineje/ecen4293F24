import networkx as nx
import matplotlib.pyplot as plt

def read_movie_data(file_path):
    """
    Reads movie data from a text file and returns a dictionary where the keys
    are movie names and the values are lists of actors in those movies.
    """
    movies = {}
    with open(file_path, 'r') as file:
        for line in file:
            movie, actors_str = line.split(':')
            actors = [actor.strip() for actor in actors_str.split(',')]
            movies[movie.strip()] = actors
    return movies

def build_graph(movies):
    """
    Builds a graph from the movie data where nodes are actors and edges represent
    movies in which the actors have starred together.
    """
    G = nx.Graph()
    for movie, actors in movies.items():
        for i in range(len(actors)):
            for j in range(i + 1, len(actors)):
                G.add_edge(actors[i], actors[j], movie=movie)
    return G

def degrees_of_bacon(G, target_actor):
    """
    Finds the shortest path (degrees of separation) from Kevin Bacon to the target actor.
    """
    try:
        path = nx.shortest_path(G, source="Kevin Bacon", target=target_actor)
        return path
    except nx.NetworkXNoPath:
        return None

def plot_graph(G, path=None):
    """
    Plots the graph and highlights the path if provided.
    """
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(G)
    
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=2000, font_size=10)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="orange")
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
    else:
        nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=2000, font_size=10)
    
    labels = nx.get_edge_attributes(G, "movie")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Six Degrees of Bacon - Actor Connections")
    plt.show()

def main():
    file_path = 'movie_data_small.txt'
    movies = read_movie_data(file_path)
    
    G = build_graph(movies)
    
    # Example actor to find degrees of separation
    target_actor = "Actor G"  # Change this to any actor present in the file
    
    path = degrees_of_bacon(G, target_actor)
    
    if path:
        print(f"Degrees of separation from Kevin Bacon to {target_actor}:")
        print(" -> ".join(path))
    else:
        print(f"No connection found between Kevin Bacon and {target_actor}.")
    
    # Plot the graph and highlight the path if it exists
    plot_graph(G, path)

if __name__ == "__main__":
    main()