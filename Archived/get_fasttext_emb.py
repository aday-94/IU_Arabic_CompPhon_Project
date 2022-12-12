import os, sys
import fasttext
import json

INPUT_TXT = 'all_transcripts.txt'
IPAS_IN_TRANSCRIPTS = 'transcripts_ipa_symbols.json'
FASTTEXT_VEC_PATH = 'fasttext_numvecs.json'
# IPA_SYMBOLS_PATH = 'fasttext_ipa_symbols.json'
MODEL_PATH = 'fasttext.bin'

with open(IPAS_IN_TRANSCRIPTS, 'r') as arb_ipas:
    arb_ipas = json.load(arb_ipas)

### use the skip-gram model 
# @ws: window size. Phonological phenomena like feature spreading/blocking doesn't occur across word boundaries, so set to 1.
# @dim: dimensions. We orginally have 29 features. Play around with this number later, but let's keep it at 20 for now.
model = fasttext.train_unsupervised(INPUT_TXT, model='skipgram', ws=1, minn=1, maxn=3, dim=29) 

### create file containing phoneme embeddings 
phoneme_embs = [] # len: 62
for phoneme in arb_ipas:
    print(phoneme)
    phoneme_embs.append( (model.get_input_vector(model.get_subword_id(phoneme))).tolist() )
print(len(phoneme_embs))
# sys.stdout = open(FASTTEXT_VEC_PATH, 'w')
# jsonString = json.dumps(phoneme_embs)
# print(jsonString)

# # ### save the model for later use
# model.save_model(MODEL_PATH)