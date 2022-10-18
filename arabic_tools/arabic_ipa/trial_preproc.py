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
    ' ّ':'', # Tashdid: geminate, ie double the previous consonant
    ' َ':'a',
    ' ً':'',
    ' ُ':'u',
    ' ٌ':'',
    ' ِ':'i',
    ' ٍ':'',
    ' ْ':'' # explicit absence of vowel
    'ـ':'',
    '':'ʔ' # Hamza = glottal stop
}

def remove_punctuations(text):
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)

def remove_repeating_char(text):
    return re.sub(r'(.)\1+', r'\1', text)

def change_diacritics(text):
    for word in text:
        for i,char in enumerate(word):
            print((ord(char),char)) # each diacritic gets treated as its own character
            if char in list(arabic_diacritics_dict.keys()):
                print(char + " is an arabic diacritic")
                if char == ' ّ':
                    char = word[i-1]
                else:
                    # print("I am a vowel diacritic\n")
                    char = arabic_diacritics_dict[char]
    return text

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