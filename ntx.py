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
    'with_labels': True,
}

G.add_weighted_edges_from(tl)
# use nested for loop like e.g. for i in range of the length of the vector , second one for index position [2]== "0.0", then cont
#for i in range(len(tl)):
#    if i == "0.0":
#        G.remove_edges(i)

nx.draw(G, arrows=True, with_labels=True)
plt.show()

#edges =  nx.to_numpy_matrix(G, nodelist= G.nodes())

#edges[edges<0] = 0

#G2 = nx.from_numpy_matrix(edges)

#pos=nx.spring_layout(G2)
#nx.draw_networkx_edges(G2, pos)
#plt.axis('off')
#plt.show()
