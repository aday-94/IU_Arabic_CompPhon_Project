import epitran
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--input_file")
parser.add_argument("--output_file")
args = parser.parse_args()

epi = epitran.Epitran('ara-Arab')

# Read in text
with open(args.input_file, 'r') as in_f, open(args.output_file, 'w') as out_f:
    # ### If split line by line
    #  while in_f:
    #     line = in_f.readline()
    #     if line == "":
    #         break
    #     out_f.write(epi.transliterate(line))

    # ### If one chunk of text
    # txt = in_f.read().split()
    # for w in txt:
    #     translated_w = epi.transliterate(w)
    #     out_f.write(translated_w + " ")