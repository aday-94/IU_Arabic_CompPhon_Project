# coding=utf-8
import re
import string
import sys
import argparse

arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
english_punctuations = string.punctuation
punctuations_list = arabic_punctuations + english_punctuations

arabic_diacritics = re.compile("""
                             ّ    | # Tashdid (geminate consonant)
                             َ    | # Fatha (a)
                             ً    | # Tanwin Fath (???)
                             ُ    | # Damma (u)
                             ٌ    | # Tanwin Damm (???)
                             ِ    | # Kasra (i)
                             ٍ    | # Tanwin Kasr (double short vowel at end of word?)
                             ْ    | # Sukun (absence of vowel)
                             ـ     # Tatwil/Kashida

                         """, re.VERBOSE)

arabic_diacritics_dict = {
    ' ّ':'', # Tashdid: geminate?, ie double the previous consonant
    u'\u0651': '', # Shadda: geminate
    ' َ':'a',
    ' ً':'',
    ' ُ':'u',
    u'\u064F':'u', # Damma
    ' ٌ':'',
    ' ِ':'i', # Kasra
    u'\u0650':'i', # Kasra
    ' ٍ':'',
    ' ْ':'', # explicit absence of vowel
    'ـ':'',
    u'\u0654':'ʔ', # Hamza above = glottal stop
    u'\u0655':'ʔ', # Hamza below = glottal stop
    u'\u0649':'ʔ', # Alef Maksura? = 
    u'\u0629':'a', # Teh Marbuta = feminine marker
    u'\u064D':'in', # Kasratan = postnasalized long vowel /i/
    u'\u064B':'an', # Fathatan = postnasalized long vowel /a/
    u'\u064D':'un', # Dammatan = postnasalized long vowel /u/
    u'\u0652':'' # Sukun = no vowel
}
print(list(arabic_diacritics_dict.keys()))

def remove_punctuations(text):
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)

def remove_repeating_char(text):
    return re.sub(r'(.)\1+', r'\1', text)

def change_diacritics(text):
    new_text = ""
    for word in text:
        for i,char in enumerate(word):
            if char == (u'\u0654' or u'\u0655'): # glottal stop
                new_text += arabic_diacritics_dict[u'\u0654'] 
            elif char == u'\u0629': # 'a'
                new_text += arabic_diacritics_dict[u'\u0629'] 
            elif char == u'\u0649': # glottal stop
                new_text += arabic_diacritics_dict[u'\u0649']
            elif char == u'\u0650': # i 
                new_text += arabic_diacritics_dict[u'\u0650']
            elif char == u'\u064F': # u
                new_text += arabic_diacritics_dict[u'\u064F']
            elif char == u'\u064D': # in
                new_text += arabic_diacritics_dict[u'\u064D']
            elif char == u'\u064B': # an
                new_text += arabic_diacritics_dict[u'\u064B']
            elif char == u'\u064D': # in
                new_text += arabic_diacritics_dict[u'\u064D']
            elif char == u'\u0651': # geminate consonant
                new_text += word[i-1]
            elif char == u'\u0652':
                continue
            else:
                new_text += char
            # print((ord(char),char)) # each diacritic gets treated as its own character    
    print(new_text)        
    return new_text

parser = argparse.ArgumentParser(description='Pre-process arabic text (remove '
                                             'diacritics, punctuations, and repeating '
                                             'characters).')

parser.add_argument('-i', '--infile', type=argparse.FileType(mode='r', encoding='utf-8'),
                    help='input file.', required=True)
parser.add_argument('-o', '--outfile', type=argparse.FileType(mode='w', encoding='utf-8'),
                    help='out file.', required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    text = args.infile.read()
    text = remove_punctuations(text)
    text = change_diacritics(text)
    # text = remove_repeating_char(text)
    args.outfile.write(text)