import csv
import networkx as nx
import matplotlib.pyplot as plt

# Initialize the graph
G = nx.Graph()

# Read the CSV data
players = []
with open('osu-roster-2024.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Clean up height and weight
        row['Height'] = int(row['Height'].replace("'", "").replace('"', '').replace(' ', ''))
        row['Weight'] = int(row['Weight'].replace(' lbs', '').strip())
        players.append(row)
        # Add a node for each player
        G.add_node(row['Name'], position=row['Position'], height=row['Height'],
                   weight=row['Weight'], hometown=row['Hometown'])

# Function to calculate height difference
def height_diff(h1, h2):
    return abs(h1 - h2)

# Function to calculate weight difference
def weight_diff(w1, w2):
    return abs(w1 - w2)

# Create edges based on shared attributes
for i in range(len(players)):
    for j in range(i + 1, len(players)):
        player1 = players[i]
        player2 = players[j]

        # Edge weight represents the strength of the connection
        edge_weight = 0

        # Check if players share the same position
        # if player1['Position'] == player2['Position']:
        #     edge_weight += 3  # Strong connection

        # Check if players are from the same hometown
        if player1['Hometown'] == player2['Hometown']:
            edge_weight += 2  # Medium connection

        # Check if players have similar height (difference <= 2 inches)
        # if height_diff(player1['Height'], player2['Height']) <= 2:
        #     edge_weight += 1  # Weak connection

        # Check if players have similar weight (difference <= 10 lbs)
        # if weight_diff(player1['Weight'], player2['Weight']) <= 10:
        #     edge_weight += 1  # Weak connection

        # Add edge if there is any connection
        if edge_weight > 0:
            G.add_edge(player1['Name'], player2['Name'], weight=edge_weight)

# Draw the graph
plt.figure(figsize=(15, 15))

# Position nodes using spring layout for better visualization
pos = nx.spring_layout(G, k=0.15, iterations=20)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=300, node_color='lightblue')

# Draw edges with transparency based on weight
edges = G.edges(data=True)
edge_colors = ['black' if edge[2]['weight'] >= 3 else 'grey' for edge in edges]
edge_alphas = [edge[2]['weight'] / 5 for edge in edges]
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, alpha=0.5)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=8)

plt.title("OSU Football Players Network Graph")
plt.axis('off')
plt.show()
