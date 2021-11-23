'''

L542 Fall 2021
Final Project
Lily Kawaoto <lkawaoto@iu.edu>
Andrew Davis <ad7@iu.edu>

"Creates a list of IPA feature vectors."

'''


import os, sys, re
from numpy.core.numeric import full
# from nltk.corpus.reader import tagged
import pandas as pd
import pprint


# change paths if necessary
CSV_PATH = './english_ipa.csv'
# OUTPUT_FILE = 'ipa_vecs.txt'


### : Read in english_ipa.csv 
# @ ipa_vecs: list of ipa feature vectors
df = pd.read_csv(CSV_PATH, engine='python')
df_len = len(df.index)

ipa_vecs = []
for i in range(df_len):
    row = df[i:i+1].values.tolist() # a list of 1 list...
    full_vec = row[0]
    feature_vec = full_vec[1:]
    ipa = full_vec[0]
    print("Creating feature vec for /{}/:".format(ipa))
    print(feature_vec)
    #ipa_vecs.append(feature_vec)
    ipa_vecs.append(full_vec) # Lily: we may want to keep the IPA symbol for later, so I'll leave it in the vector

print(ipa_vecs)



