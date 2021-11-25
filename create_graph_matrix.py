'''

L542 Fall 2021
Final Project
Lily Kawaoto <lkawaoto@iu.edu>

"Creates a matrix of node-to-node relationship statements.
 Format of relationship statement: [node1, node2, edge weight]
 Edge weight is the normalized weight between an IPA symbol and a specific feature."

'''

import os, sys, re
from numpy.core.numeric import full
import pandas as pd
import pprint


# change paths if necessary
CSV_PATH = './norm_vecs.txt'