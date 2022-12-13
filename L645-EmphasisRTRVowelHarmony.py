""" L645 ANLP Comp Phon Final Project Fall 2022 Andrew Davis -- Step 7: List of Regex for applying Emphatic Vowel Harmony to Arabic IPA  """


import re

IN = open('f2k22data-step6-arbipa-removedpunct-phone1-gem.txt', encoding = 'utf-8')
OUT = open('f2k22data-step7-arbipa-phon2-emphaticvowelharmony.txt', 'w')

text = IN.read()
#print(text)

words = text.split()
print(words)
#I have a text, I need to look at each word, if an emphatic is in the word, replace the vowels in that word with uvularized vowels
def msa_emphatic_vowel_harmony_ipa(words):
    th_emphatic_ipa = re.compile("ðˤ", re.VERBOSE)
    t_emphatic_ipa = re.compile("tˤ", re.VERBOSE)
    d_emphatic_ipa = re.compile("dˤ", re.VERBOSE)
    s_emphatic_ipa = re.compile("sˤ", re.VERBOSE)
    new_words = []
    
    for word in words:
        
        new_word = word
        if th_emphatic_ipa.findall(word):
            new_word = re.sub('i', 'iʶ', new_word)
            new_word = re.sub('u', 'uʶ', new_word)
            new_word = re.sub('a', 'aʶ', new_word)
        
        elif t_emphatic_ipa.findall(word):
            new_word = re.sub('i', 'iʶ', new_word)
            new_word = re.sub('u', 'uʶ', new_word)
            new_word = re.sub('a', 'aʶ', new_word)
        
        elif d_emphatic_ipa.findall(word):
            new_word = re.sub('i', 'iʶ', new_word)
            new_word = re.sub('u', 'uʶ', new_word)
            new_word = re.sub('a', 'aʶ', new_word)
        
        elif s_emphatic_ipa.findall(word):
            new_word = re.sub('i', 'iʶ', new_word)
            new_word = re.sub('u', 'uʶ', new_word)
            new_word = re.sub('a', 'aʶ', new_word)
        
        new_words.append(new_word + ' ')
        
    print(new_word, word)
    return new_words

msa_emphatic_vowel_ipa_words = msa_emphatic_vowel_harmony_ipa(words)
        
print(msa_emphatic_vowel_harmony_ipa(words))

for w in msa_emphatic_vowel_ipa_words:
    OUT.write(w)

IN.close()
OUT.close()