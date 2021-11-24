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


### : Read in english_ipa.csv 
df = pd.read_csv(CSV_PATH, engine='python')
df_len = len(df.index)


### : Create raw vector from csv file
# @ ipa_vecs: list of ipa feature vectors with values +, -, or 0
ipa_vecs = []
for i in range(df_len):
    row = df[i:i+1].values.tolist() # a list of 1 list... why?
    full_vec = row[0]
    feature_vec = full_vec[1:]
    ipa = full_vec[0]
    # print("Creating feature vec for /{}/:".format(ipa))
    # print(feature_vec)

    # note (Lily): we may want to keep the IPA symbol for later, so I'll leave it in the vector
    #ipa_vecs.append(feature_vec)
    ipa_vecs.append(full_vec) 
# print(type(ipa_vecs))
# print(ipa_vecs)


### : Create modified vector using 3 numerical features
# @ num_vecs: list of IPA feature vectors with values 1, -1, or 0
#             first value in vector is the IPA symbol
length = len(ipa_vecs[0])
num_vecs = []
for ipa in ipa_vecs:
    temp = []
    for i in range(length):
        if ipa[i]=='-':
            ipa[i] = -1
        elif ipa[i]=='+':
            ipa[i] = 1
        temp.append(ipa[i])
    num_vecs.append(temp)
# print(num_vecs)


### : Create modified vector using 2 numerical featurse
# @ num_binary_vecs: list of IPA feature vectors with values 1 or 0
#                    collapsed -1 and 0 to be feature 0
num_binary_vecs = []
for ipa in num_vecs:
    temp = []
    for i in range(length):
        if ipa[i] == -1:
            ipa[i] = 0
        temp.append(ipa[i])
    num_binary_vecs.append(temp)
# print(num_binary_vecs)