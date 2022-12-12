'''

L700 Spring 2022
Final Project
Lily Kawaoto <lkawaoto@iu.edu>

"Creates 2 files: (1) IPA phoneme embeddings (inputs) 
                  (2) their corresponding IPA symbol in ASCII format"

'''

import os, sys, re
from numpy.core.numeric import full
import pandas as pd
import json
import pprint

# change/uncomment paths as necessary
"""
@ IPA_CSV_PATH: csv file containing our feature chart for Arabic
@ NORM_VEC_PATH: json file containing normalized vectors for each IPA symbol (input)
@ IPA_SYMBOLS_PATH: json file containing the IPA symbols (target)
"""
# ******************************************************* #
#           FALL 2021 VER.   
# IPA_CSV_PATH = './L2_arb_ipa_F21.csv' 
# NUM_VEC_PATH = './L2_arb_numvecs_F21.json'
# IPA_SYMBOLS_PATH = './L2_arb_ipa_symbols_F21.json' # ie, list of phonemes
# ******************************************************* #
# ******************************************************* #
#           SPRING 2022 VER.
IPA_CSV_PATH = './L2_arb_ipa_S22.csv'
NUM_VEC_PATH = './L2_arb_numvecs_S22.json'
IPA_SYMBOLS_PATH = './L2_arb_ipa_symbols_S22.json' 
# ******************************************************* #
# ******************************************************* #
#           PHOIBLE VER.
# IPA_CSV_PATH = 'phoible_ipa_features.csv'
# NUM_VEC_PATH = 'phoible_numvecs.json'
# IPA_SYMBOLS_PATH = 'phoible_ipa_symbols.json'
# ARB_SYMBOLS_PATH = './S22_ver/L2_arb_ipa_symbols_S22.json'
# ******************************************************* #
# ******************************************************* #
#           PANPHON VER.
# IPA_CSV_PATH = 'panphon_ipa_features.csv'
# NUM_VEC_PATH = 'panphon_numvecs_S22.json'
# IPA_SYMBOLS_PATH = 'panphon_ipa_symbols.json'
# ARB_SYMBOLS_PATH = './S22_ver/L2_arb_ipa_symbols_S22.json'
# ******************************************************* #


# def normalize_vec(li): 
#     max_value = max(li)
#     min_value = min(li)
#     for i in range(len(li)):
#         li[i] = (li[i] - min_value) / (max_value - min_value)
#     return li 


### : Read in feature chart csv 
df = pd.read_csv(IPA_CSV_PATH, engine='python')

### : If creating vecs from outside source, keep the Arabic IPA symbols
if 'ARB_SYMBOLS_PATH' in globals(): 
    with open(ARB_SYMBOLS_PATH, 'r') as arb:
        arb_ipas = json.load(arb) #len=41
    arb_ipas.append('dʒ') # hardcode this symbol bc of affricate diacritic
    if IPA_CSV_PATH == 'phoible_ipa_features.csv':
        filtered = df['segment'].isin(arb_ipas)
    elif IPA_CSV_PATH == 'panphon_ipa_features.csv':
        filtered = df['ipa'].isin(arb_ipas)
    df = df[filtered]

df_len = len(df.index)
df_feat_names = list(df.iloc[0].tolist())

### : Create raw vector from csv file
# @ ipas: list of ipa symbols
# @ feature_vecs: list of ipa feature vectors with values +, -, or 0
ipas = []
feature_vecs = []
i = 1
while i < df_len:
    full_vec = df[i:i+1].values.tolist()[0]
    ipa = full_vec[0]
    fv = full_vec[1:]
    feature_vecs.append(fv) 
    ipas.append(ipa)
    i += 1

sys.stdout = open(IPA_SYMBOLS_PATH, 'w')
jsonString = json.dumps(ipas) # json.dumps() has an ensure-ASCII param
print(jsonString)


### : Create modified vector using 3 numerical features 
# @ numerical_vecs: list of IPA feature vectors with values 1, -1, or 0.
#                   The first value in vector is the IPA symbol
# !!! UPDATE 11/25/21 -- use 4 numbers (2, 1, -1, 0) to mimic feature geometry tree. 
num_features = len(feature_vecs[0])
numerical_vecs = []
for vec in feature_vecs:
    temp = []
    for i in range(num_features):
        if vec[i] == '-':
            temp.append(-1)
        elif vec[i] == '+':
            if df_feat_names[i+1].isupper():
                temp.append(2)
            else:
                temp.append(1)
        else:
            temp.append(0)
    numerical_vecs.append(temp)
sys.stdout = open(NUM_VEC_PATH, 'w')
jsonString = json.dumps(numerical_vecs) # json.dumps() has an ensure-ASCII param
print(jsonString)