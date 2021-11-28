import networkx as nx
import matplotlib.pyplot as plt
import json

TRIPLETS_PATH = './triplets.json'

# Create Graph
G = nx.DiGraph()
ipa_nodes = []
feature_nodes = []

# Load the triplets
with open(TRIPLETS_PATH, 'r') as trip:
    tl = json.load(trip)
#print(tl)

options = {
    'node_color': 'blue',
    'node_size': 10,
    'width': 3,
    'arrowstyle': '-|>',
    'arrowsize': 10,
}

G.add_weighted_edges_from(tl)
nx.draw_networkx(G, arrows=True, **options)
plt.show()


