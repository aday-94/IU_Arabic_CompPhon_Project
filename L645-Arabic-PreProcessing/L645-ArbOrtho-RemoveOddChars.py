""" L645 ANLP Comp Phon Final Project Fall 2022 Andrew Davis -- Step 2: Regex for Converting/Removing Odd Arabic Script Characters in Arabic Orthographic Text """

import re

IN = open('f2k22data-step1-arbortho-engrem.txt', encoding = 'utf-8')
OUT = open('f2k22data-step2-arbortho-engrem-oddcharsrem.txt', 'w')

text = IN.read()

""" Step 2 Preprocessing: Convert/Remove Odd Arabic Script Characters from Arabic Orthographic Text """

def arab_ortho_odd_characters(text):

    threedots = re.compile("""ۛ""", re.VERBOSE) #CONFIRMED WORKS
    lig_quranicstop_qala = re.compile("""ۗ""", re.VERBOSE) #CONFIRMED WORKS -- Cut off sound at end of word for breathing mainly for recitation
    lig_quranicstop_sala = re.compile("""ۖ""", re.VERBOSE) #CONFIRMED WORKS -- Cut off sound at end of word for breathing mainly for recitation
    lig_jim = re.compile("""ۚ""", re.VERBOSE) #CONFIRMED WORKS
    lig_mim = re.compile("""ۘ""", re.VERBOSE) #CONFIRMED WORKS
    soviet = re.compile("☭", re.VERBOSE) #CONFRIMED WORKS
    dash = re.compile("—", re.VERBOSE)

    text = re.sub(threedots, "", text)
    text = re.sub(lig_quranicstop_qala, "", text)
    text = re.sub(lig_quranicstop_sala, "", text)
    text = re.sub(lig_jim, "", text)
    text = re.sub(lig_mim, "", text)
    text = re.sub(soviet, "", text)
    text = re.sub(dash, "", text)

    return text

#print(arab_ortho_odd_characters(text))

text_no_odds = arab_ortho_odd_characters(text)

def arab_ortho_removewords_persianchars(text_no_odds):

    ye_persian = re.compile("ی", re.VERBOSE)
    kaf_persian = re.compile("ک", re.VERBOSE)

    words = text_no_odds.split()
    new_words = []
    
    for word in words:
        new_word = word
        
        if ye_persian.findall(word):
            new_word = re.sub(word, " ", new_word)
        
        elif kaf_persian.findall(word):
            new_word = re.sub(word, " ", new_word)
        
        new_words.append(new_word + " ")
        
    print(new_word, word)
    return new_words
    
finaltext_no_odd = arab_ortho_removewords_persianchars(text_no_odds)
print(finaltext_no_odd)

for w in finaltext_no_odd:
    OUT.write(w)

IN.close()
OUT.close()