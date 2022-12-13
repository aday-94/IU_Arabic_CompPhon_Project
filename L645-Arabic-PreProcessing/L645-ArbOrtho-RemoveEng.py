""" L645 ANLP Comp Phon Final Project Fall 2022 Andrew Davis -- Step 1: Regex for Removing English Characters in Arabic Orthographic Text """

import re

IN = open('f2k22data-arbortho.txt', encoding = 'utf-8')
OUT = open('f2k22data-step1-arbortho-engrem.txt', 'w')

text = IN.read()

""" Step 1 Preprocessing: Remove English Characters from Arabic Orthographic Text """

def arab_ortho_remove_eng(text):
    
    english_chars = re.compile("[A-Za-z]", re.VERBOSE)

    text = re.sub(english_chars, "", text)

    return text

print(arab_ortho_remove_eng(text))

arab_ortho_text_no_eng = arab_ortho_remove_eng(text)

for w in arab_ortho_text_no_eng:
    OUT.write(w)

IN.close()
OUT.close()