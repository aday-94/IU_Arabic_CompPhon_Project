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
OUTPUT_PATH = './norm_vecs.txt'


def normalize_vec(li): 
    max_value = max(li)
    min_value = min(li)
    for i in range(len(li)):
        li[i] = (li[i] - min_value) / (max_value - min_value)
    return li 


### : Read in english_ipa.csv 
df = pd.read_csv(CSV_PATH, engine='python')
df_len = len(df.index) # 37 IPA symbols
df_cols = list(df.columns) # len = 24: 1 IPA + 23 features


### : Create raw vector from csv file
# @ feature_vecs: list of ipa feature vectors with values +, -, or 0
#                 24 columns = 24 features
# @ ipa_list: list of ipa symbols
ipa_list = []
feature_vecs = []
for i in range(df_len):
    full_vec = df[i:i+1].values.tolist()[0] # w/o [0], returns a list of 1 list
    ipa = full_vec[0]
    feature_vec = full_vec[1:]
    # print("Creating feature vec for /{}/:".format(ipa))
    # print(feature_vec)
    feature_vecs.append(feature_vec) 
    ipa_list.append(ipa)


### : Create modified vector using 3 numerical features 
# @ num_vecs: list of IPA feature vectors with values 1, -1, or 0
#             the first value in vector is the IPA symbol
### : UPDATE 11/25/21 -- use 4 numbers (2, 1, -1, 0). normalize vectors in next step.
num_features = len(feature_vecs[0])
numerical_vecs = []
for vec in feature_vecs:
    temp = []
    for i in range(num_features):
        if vec[i]=='-':
            vec[i] = -1
        elif vec[i]=='+':
            if df_cols[i+1].isupper():
                vec[i] = 2
            else:
                vec[i] = 1
        else:
            vec[i] = 0
        temp.append(vec[i])
    numerical_vecs.append(temp)
# print(numerical_vecs)

### : Normalize vector
norm_vecs = [normalize_vec(v) for v in numerical_vecs]
sys.stdout = open(OUTPUT_PATH, 'w')
print(norm_vecs)
sys.stdout.close()
