"""
References:
    1. Garber, L. (2019). CHA file python parser. Zenodo. https://doi.org/10.5281/zenodo.3364020
       (slight modifications made to translate Spanish into English)
    2. Sofroniev, Pavel. (2016). https://pypi.org/project/ipatok/
"""

CHA_FILE_DIR = '/Users/lilykawaoto/Documents/GitHub/CompPhon/CHAFile'
TRANSCRIPTS_PATH_FROM_DIR = '../CHILDES corpus transcripts'

from dataclasses import replace
import os, sys, re
import string
sys.path.insert(0, CHA_FILE_DIR)
from ChaFile import *
from ipatok import tokenise
# !pip install ipatok


def preprocess(utt):
    remove_punctuation = "!\"#$%&'()*+, -./;<=>?@[\]^_`{|}~ˈ‘’"
    utt = re.sub(r'@s:eng', '', utt) # code switching or English loanwords?
    utt = re.sub(r'ˤˤ', r'ˤ',utt) # otherwise, tokenizer thinks a symbol has 2 diacritics (e.g. [ʔˤˤ])
    utt = re.sub(r'ːː', r'ː',utt)
    utt = re.sub(r'xxx','',utt)
    translator = utt.maketrans('', '', remove_punctuation)
    return utt.translate(translator).lower()

def tokenize(utt):
    tok = []
    length = len(utt)
    cnt = 0
    while cnt < length:
        if (cnt+1 < length) and (utt[cnt+1] == 'ː'):
            tok.append(utt[cnt:cnt+1])
            cnt +=2
        else:
            tok.append(utt[cnt])
            cnt += 1
    return tokenize    

files = [file for file in  os.listdir(TRANSCRIPTS_PATH_FROM_DIR) if file.endswith('.cha')]
utterances  = []
for f in files:
    cha = ChaFile(f)
    lines = cha.getLines() # list of dicts
    utterances.extend([preprocess(dct['utterance']) for dct in lines])

phonemes = [tokenise(u, replace=True, diphthongs=True) for u in utterances] 
phonemes = set([preprocess(p) for phon in phonemes for p in phon])
"""
# print(phonemes) 

{'nː', 'h', 'f', 'ɣ', 'ɡ', 'i', 'ʃ', 'lː', 'ħ', 'o', 'dː', 'sː', 'tː', 'oː', 'ʕ', 'l', 'p', 'uː', 'j', 'ʔː', 'ʒ', 'x', 'ʊ', 'u', 'jː', 'ʔ', 'e', 'm', 'dˤ', 'ɔ', 'y', 'd͡ʒ', 'ð', 'b', 'ʒː', 'iː', 'æ', 'k', 's', 'eː', 'd', 'aː', 'θ', 'ɛ', 'r', 'n', 'ɑ', 'w', 'ɪ', 'v', 'ə', 'mː', 'sˤ', 't', 'ʌ', 'c', 'zˤ', 'a', 'z', 'q', 'æː', 'tˤ'}
"""

