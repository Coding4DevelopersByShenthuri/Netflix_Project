import networkx as nx
import matplotlib.pyplot as plt  

# Function to create a network graph of actors/directors
def create_network(df):
    """
    Creates a network graph of actors based on shared cast appearances.

    Parameters:
    - df: DataFrame, contains a column 'cast' with comma-separated actor names

    Returns:
    - G: networkx.Graph, generated graph based on shared appearances
    """
    G = nx.Graph()
    
    # Iterate through rows to add edges based on cast members
    for _, row in df.iterrows():
        cast_members = row['cast'].split(', ') if row['cast'] else []
        for i in range(len(cast_members)):
            for j in range(i + 1, len(cast_members)):
                G.add_edge(cast_members[i], cast_members[j])
    
    return G

# Visualize the network
def plot_network(G):
    """
    Visualizes the actor/director network.

    Parameters:
    - G: networkx.Graph, the graph to be visualized
    """
    plt.figure(figsize=(12, 12))
    nx.draw(G, with_labels=True, node_size=20, font_size=10)
    plt.title("Network of Actors/Directors")
    plt.show()
