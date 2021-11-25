'''

L542 Fall 2021
Final Project
Lily Kawaoto <lkawaoto@iu.edu>

"Creates a list of IPA feature vectors."

'''


import os, sys, re
from numpy.core.numeric import full
# from nltk.corpus.reader import tagged
import pandas as pd
import pprint


# change paths if necessary
CSV_PATH = './english_ipa.csv'


def normalize_vec(li): 
    max_value = max(li)
    min_value = min(li)
    for i in range(len(li)):
        li[i] = (li[i] - min_value) / (max_value - min_value)
    return li 


### : Read in english_ipa.csv 
df = pd.read_csv(CSV_PATH, engine='python')
df_len = len(df.index)
df_cols = list(df.columns)


### : Create raw vector from csv file
# @ ipa_vecs: list of ipa feature vectors with values +, -, or 0
#             37 columns = 1 IPA symbol + 36 features
ipa_vecs = []
for i in range(df_len):
    row = df[i:i+1].values.tolist() # a list of 1 list... why?
    full_vec = row[0]
    feature_vec = full_vec[1:]
    ipa = full_vec[0]
    # print("Creating feature vec for /{}/:".format(ipa))
    # print(feature_vec)

    ## note: we may want to keep the IPA symbol for later, so I'll leave it in the vector
    # ipa_vecs.append(feature_vec)
    ipa_vecs.append(full_vec) 


### : Create modified vector using 3 numerical features 
# @ num_vecs: list of IPA feature vectors with values 1, -1, or 0
#             the first value in vector is the IPA symbol
### : UPDATE 11/25/21 -- use 4 numbers (2, 1, -1, 0). normalize vectors in next step.
length = len(ipa_vecs[0])
num_vecs = []
for ipa in ipa_vecs:
    temp = []
    for i in range(length):
        if i==0:
            continue
        elif ipa[i]=='-':
            ipa[i] = -1
        elif ipa[i]=='+':
            if df_cols[i].isupper():
                ipa[i] = 2
            else:
                ipa[i] = 1
        else:
            ipa[i] = 0
        temp.append(ipa[i])
    num_vecs.append(temp)
# print(num_vecs)


### : Normalize vector
norm_vec = [normalize_vec(v) for v in num_vecs]
print(norm_vec)