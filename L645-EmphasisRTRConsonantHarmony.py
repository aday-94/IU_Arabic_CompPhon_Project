import re

IN = open('f2k22data-arbipa-diacriticipa.txt', encoding = 'utf-8')
#OUT = open('f2k22data-arbortho-diacriticipa.txt', 'w')

text = IN.read()
#print(text)

words = text.split()
#print(words)
#I have a text, I need to look at each word, if an emphatic is in the word, replace the l and/or r's in that word with pharyngealized counterpart
def msa_emphatic_liquid_harmony_ipa(words):
    th_emphatic_ipa = re.compile("ðˤ", re.VERBOSE)
    t_emphatic_ipa = re.compile("tˤ", re.VERBOSE)
    d_emphatic_ipa = re.compile("dˤ", re.VERBOSE)
    s_emphatic_ipa = re.compile("sˤ", re.VERBOSE)
    new_words = []
    
    for word in words:
        
        new_word = word
        if th_emphatic_ipa.findall(word):
            new_word = re.sub('l', 'lˤ', new_word)
            new_word = re.sub('r', 'rˤ', new_word)
        
        elif t_emphatic_ipa.findall(word):
            new_word = re.sub('l', 'lˤ', new_word)
            new_word = re.sub('r', 'rˤ', new_word)
        
        elif d_emphatic_ipa.findall(word):
            new_word = re.sub('l', 'lˤ', new_word)
            new_word = re.sub('r', 'rˤ', new_word)
        
        elif s_emphatic_ipa.findall(word):
            new_word = re.sub('l', 'lˤ', new_word)
            new_word = re.sub('r', 'rˤ', new_word)
        
        new_words.append(new_word)
        
    
        
    #print(new_word, word)
    return new_words

msa_emphatic_liquid_ipa_words= msa_emphatic_liquid_harmony_ipa(words)
        
print(msa_emphatic_liquid_harmony_ipa(words))