'''

L542 Fall 2021
Final Project
Lily Kawaoto <lkawaoto@iu.edu>

"Creates a matrix of node-to-node relationship statements.
 Format of relationship statement: [node1, node2, edge weight]
 Edge weight is the normalized weight between an IPA symbol and a specific feature."

'''

import os, sys, re, json
from numpy.core.numeric import full
import pandas as pd
import pprint


# change paths if necessary
VEC_PATH = './norm_vecs.json'
IPA_PATH = './ipa_symbols.json'
CSV_PATH = './english_ipa.csv'
TRIPLETS_PATH = './triplets.json'

### : Read in norm_vecs.json
with open(VEC_PATH, 'r') as f:
    norm_vecs = json.load(f)

### : Read in xsampa_symbols.csv
with open(IPA_PATH, 'r') as f:
    ipas = json.load(f) # load() converts ASCIIs to chars

### : Read in english_ipa.csv to get feature names
# # @ features: list of column names ['syl', ... 'tense'] (excludes 'ipa')
df = pd.read_csv(CSV_PATH, engine='python')
df_len = len(df.index) # 37 IPA symbols
features = list(df.columns)[1:] # 23 features
num_features = len(features)


### : Create triplet [node1, node2, edge_weight]
#           @ node1: ipa symbol
#           @ node2: feature
#           @ edge_weight: normalized weight
# # @ triplets: list of triplets
triplets = []
for i in range(df_len):
    for j in range(num_features):
        triplets.append((ipas[i], features[j], norm_vecs[i][j]))

sys.stdout = open(TRIPLETS_PATH, 'w')
jsonString = json.dumps(triplets) # json.dumps() has an ensure-ASCII param
print(jsonString)
sys.stdout.close()