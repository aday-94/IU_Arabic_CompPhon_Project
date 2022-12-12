#!/usr/bin/env python
# Usage: python ocpcluster.py textfile.txt
# Splits segments by OCP-based algorithm and draws hierarchical graph
# Dependencies: pydot (for cluster drawing)
# The input file is assumed to be unpunctuated text, possibly with
# newlines (they are ignored).
# -MH 20150502

"""
# Original code from https://github.com/cvocp/cvocp 
# Modified by Lily Kawaoto
"""

import re
import random
import itertools
import codecs
import pydot
import os
import sys

class listset:
    def __init__(self, text):
        self.text = text.split()
        self.allsegments, bigrams = self.get_ar_segments(self.text)         
        # print(self.allsegments)
        # print(bigrams)
        self.bigramcounts = {}
        for bi in bigrams:
            if bi[0] != ' ' and bi[1] != ' ':
                self.bigramcounts[bi] = self.bigramcounts.get(bi, 0) + 1
        self.tree = {}
        self.tree[''] = self.allsegments
        self.tree['0'], self.tree['1'] = self._randsplitset(self.allsegments)

    """
    def clean(self, text):
        misc_chars = ['?', '_', '"', ':', 'ː', '«', 'ﺃ', '”', ',', '“', ';', '؛', '»', "'", 'ھ', '-', 'ـ']
        misc_chars.append('ڨ')
        for misc in misc_chars:
            if misc in text:
                if misc=='?':
                    text = re.sub('\?', "", text)
                else:
                    text = re.sub(misc, "", text)
    """

    # gets Arabic segments; accounts for char groupings when emphatic, uvular, geminate, or affriate diacritic is present
    # also gets bigrams of these segments
    #       @text: list of words in input file
    def get_ar_segments(self, text):
        segments = []
        bigram_list = []

        for word in text: 
            reversed_word = word[::-1]
            ind = 0

            while ind < len(reversed_word): 
                if reversed_word[ind] == ' ':
                    ind += 1
                    continue
                elif reversed_word[ind] == 'ˤ' or reversed_word[ind] == 'ʶ' or reversed_word[ind] == 'ː':
                    if reversed_word[ind+1]=='ː':
                        ind += 1
                        continue
                    elif reversed_word[ind]=='ː' and reversed_word[ind+1]=='ʶ':
                        grouped_chars = reversed_word[ind] + reversed_word[ind+1] + reversed_word[ind+2]
                        segments.append(grouped_chars[::-1])
                        bigram_list.append(grouped_chars[::-1])
                        ind += 2
                    elif reversed_word[ind+1]=='ʒ':
                        grouped_chars = reversed_word[ind] + reversed_word[ind+1] + reversed_word[ind+2] + reversed_word[ind+3]
                        segments.append(grouped_chars[::-1])
                        bigram_list.append(grouped_chars[::-1])
                        ind += 3
                    else:
                        grouped_chars = reversed_word[ind] + reversed_word[ind+1]
                        segments.append(grouped_chars[::-1])
                        bigram_list.append(grouped_chars[::-1])
                        ind += 1
                elif reversed_word[ind] == 'ʒ':
                    grouped_chars = reversed_word[ind] + reversed_word[ind+1] + reversed_word[ind+2]
                    segments.append(grouped_chars[::-1])
                    bigram_list.append(grouped_chars[::-1])
                    ind += 2
                else:
                    segments.append(reversed_word[ind])
                    bigram_list.append(reversed_word[ind])
                
                ind += 1
        
        bigram_list.reverse()
        bigrams = [(x[0], x[1]) for x in zip(bigram_list, bigram_list[1:])]
        return set(segments), bigrams


    def split(self, set1):
        self.tree[set1 + '0'] = self.tree[set1]
        self.tree[set1 + '1'] = set()
        #self.tree[set1 + '0'], self.tree[set1 + '1'] = self._randsplitset(self.tree[set1])
               
    def _randomswap(self, n, set1, set2):
        if len(set1) == 0:
            one = set([])
        else:
            maxn = min(n, len(set1)-1)
            numswap1 = random.randint(0, maxn)
            one = set(random.sample(set1, numswap1))
        if len(set2) == 0:
            two = set([])
        else:
            maxn = min(n, len(set2)-1)
            numswap2 = random.randint(0, maxn)
            two = set(random.sample(set2, numswap2))
        return (set1 - one) | two, (set2 - two) | one

    def _score(self, set1, set2):
        sc = 0
        for bi in self.bigramcounts:
            if (bi[0] in set1 and bi[1] in set2) or (bi[0] in set2 and bi[1] in set1):
                sc += self.bigramcounts[bi]
        return sc

    def _randsplitset(self, s):
        """Splits a set randomly into two subsets."""
        setlist = list(s)
        random.shuffle(setlist)
        R = random.randint(0,len(setlist))
        return set(setlist[0:R]), set(setlist[R:])
   
with codecs.open(sys.argv[1], "r", "utf-8") as myfile:
    data = " ".join(line.rstrip() for line in myfile)


ls = listset(data)

def genperms(x):    
    barelist = ["".join(seq) for n in range(1,x) for seq in itertools.product("01", repeat=n)]    
    return [(barelist[i], barelist[i+1]) for i in range(0, len(barelist),2)]

for sets in genperms(9):
    if sets[0] in ls.tree and sets[1] in ls.tree:
        zero = ls.tree[sets[0]]
        one = ls.tree[sets[1]]
        bestzero = zero
        bestone = one
        for iter in range(1200):
            bestscore = ls._score(zero, one)
            for i in range(150):
                rs = int(1+(1/float(iter + 1))*2000) # Annealing schedule determines how many swaps to make
                newzero, newone = ls._randomswap(rs, zero, one)
                newscore = ls._score(newzero, newone)
                if newscore > bestscore:
                    bestzero = newzero
                    bestone = newone
                    print(bestscore, newscore, '{', ' '.join(newzero), '}', '{' , ' '.join(newone), '}', iter, rs)
                    #print bestscore, newscore, newzero, newone, iter, rs
                    bestscore = newscore
            zero = bestzero
            one = bestone
        if ls.tree[sets[0]] != zero and ls.tree[sets[0]] != one:
            ls.tree[sets[0]] = zero
            ls.tree[sets[1]] = one
            if len(zero) > 1:
                ls.split(sets[0])
                print("SPLITTING:", sets[0])
            if len(one) > 1:
                ls.split(sets[1])
                print("SPLITTING:", sets[1])

for par in genperms(8):    
    for p in par:
        if p in ls.tree and p + '0' in ls.tree and p + '1' in ls.tree:
            if ls.tree[p + '0'] == ls.tree[p] or ls.tree[p + '1'] == ls.tree[p]:
                del ls.tree[p + '0']
                del ls.tree[p + '1']


for k in sorted(ls.tree.keys()):
    print(k + ":"),
    for w in sorted(list(ls.tree[k])):
        print(w)
    # print
    
graph = pydot.Dot(graph_type='graph')

for k in ls.tree:
    s0 = u"\u00a0".join(sorted(list(ls.tree[k])))
    # s0 = s0.encode('utf-8')    
    if k + '0' in ls.tree:
        s00 = u"\u00a0".join(sorted(list(ls.tree[k + '0'])))
        # s00 = s00.encode('utf-8')
        edge = pydot.Edge(s0,s00)
        graph.add_edge(edge)
    if k + '1' in ls.tree:
        s01 = u"\u00a0".join(sorted(list(ls.tree[k + '1'])))
        # s01 = s01.encode('utf-8')
        edge = pydot.Edge(s0,s01)
        graph.add_edge(edge)

graph.write_pdf("arabic_graph_CV_preSS.pdf")
os.system("open arabic_graph_CV_preSS.pdf")