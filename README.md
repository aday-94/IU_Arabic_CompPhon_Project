# L542-Final-Project
Indiana University, Bloomington 

Fall 2021 L542

Lily Kawaoto, Andrew Davis

'''
STEPS:

1. create_vecs.py:
- Creates a list of IPA symbols and puts it in ipa_symbols.json
- Creates a normalized feature vector of IPA symbols and puts it in norm_vecs.json
- Import sys, pandas, numpy, json

'''

2. create_graph_matrix.py:
- Creates a matrix of node-to-node relationship statements using normalized feature values from Step 1.
- Format of relationship statement: [Node1, Node2, EdgeWeight]
