"""
References:
David R. Mortensen, Siddharth Dalmia, and Patrick Littell. 2018. Epitran: Precision G2P for many languages. In Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018), Paris, France. European Language Resources Association (ELRA).
"""

CV_TSV_PATH = '/Users/lilykawaoto/Documents/GitHub/CompPhon/CV_transcripts/train.tsv'
CV_TXT_PATH = '/Users/lilykawaoto/Documents/GitHub/CompPhon/CV_transcripts/CV_transcripts.txt'
CV_IPA_PATH = '/Users/lilykawaoto/Documents/GitHub/CompPhon/CV_transcripts/CV_transcript_ipa.txt'

from dataclasses import replace
import os, sys, re
import csv
import string
import json
from ipatok import tokenise
import epitran

"""
# def preprocess(utt):
#     remove_punctuation = "!\"#$%&'()*+, -./;<=>?@[\]^_`{|}~ˈ‘’"
#     utt = re.sub(r'@s:eng', '', utt) # code switching or English loanwords?
#     utt = re.sub(r'ˤˤ', r'ˤ',utt) # otherwise, tokenizer thinks a symbol has 2 diacritics (e.g. [ʔˤˤ])
#     utt = re.sub(r'ːː', r'ː',utt)
#     utt = re.sub(r'xxx','',utt)
#     translator = utt.maketrans('', '', remove_punctuation)
#     return utt.translate(translator).lower()
"""

"""
# def tokenize(utt):
#     tok = []
#     length = len(utt)
#     cnt = 0
#     while cnt < length:
#         if (cnt+1 < length) and (utt[cnt+1] == 'ː'):
#             tok.append(utt[cnt:cnt+1])
#             cnt +=2
#         else:
#             tok.append(utt[cnt])
#             cnt += 1
#     return tokenize 
"""   


"""
Step 1: put all transcripts in a text file 
"""
sentences_ar = []
with open(CV_TSV_PATH, 'r') as f:
    next(f) # skip header
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        sentences_ar.append(row[2])

### Uncomment to re-create file
with open(CV_TXT_PATH, 'w') as f:
    f.write(("\n".join(sentences_ar)))


"""
Step 2: convert orthographic transcriptions to IPA
"""
epi = epitran.Epitran('ara-Arab')
sentences_ipa = []
with open(CV_TXT_PATH, 'r') as f:
    while f:
        line = f.readline()
        if line == "":
            break
        ipa_transcription = epi.transliterate(line)
        sentences_ipa.append(ipa_transcription)

with open(CV_IPA_PATH, 'w') as f:
    f.write(("".join(sentences_ipa)))


# phonemes = [tokenise(u, replace=True, diphthongs=True) for u in utterances] 
# phonemes = set([preprocess(p) for phon in phonemes for p in phon])


# sys.stdout = open(IPAS_IN_TRANSCRIPTS, 'w')
# jsonString = json.dumps(list(phonemes))
# print(jsonString) 
# """
# {'nː', 'h', 'f', 'ɣ', 'ɡ', 'i', 'ʃ', 'lː', 'ħ', 'o', 'dː', 'sː', 'tː', 'oː', 'ʕ', 'l', 'p', 'uː', 'j', 'ʔː', 'ʒ', 'x', 'ʊ', 'u', 'jː', 'ʔ', 'e', 'm', 'dˤ', 'ɔ', 'y', 'd͡ʒ', 'ð', 'b', 'ʒː', 'iː', 'æ', 'k', 's', 'eː', 'd', 'aː', 'θ', 'ɛ', 'r', 'n', 'ɑ', 'w', 'ɪ', 'v', 'ə', 'mː', 'sˤ', 't', 'ʌ', 'c', 'zˤ', 'a', 'z', 'q', 'æː', 'tˤ'}
# """

