#!/usr/bin/python3

from __future__ import print_function
import sys
import json
import argparse
import os

if sys.version_info <= (3, 0):
    print("This program only runs in python3", file=sys.stderr)
    exit(1)
INPUT_FILE = "/Users/lilykawaoto/Documents/GitHub/CompPhon/CV_transcripts/ar_sample_txt.txt"
OUTPUT_FILE = "/Users/lilykawaoto/Documents/GitHub/CompPhon/CV_transcripts/ar_sample_ipa.txt"

script_dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(script_dir, "arabic-ipa.json")) as f:
    mapping = json.loads(f.read())
with open(os.path.join(script_dir, "vowels.json")) as f:
    vowels = json.loads(f.read())
with open(os.path.join(script_dir, "diacritics.json")) as f:
    diacritics = json.loads(f.read())
with open(os.path.join(script_dir, "diphthongs.json")) as f:
    diphthongs = json.loads(f.read())


def arabic_to_ipa(line, seperator=" ", keep_unknown=False):
    output_line = []
    line_len = len(line)
    next_is_vowel = False
    next_is_diphthong = False
    for i, char in enumerate(line):
        mapped = ""
        next_char = (i + 1) < line_len and line[i + 1]
        if next_is_diphthong:
            next_is_diphthong = False
            continue
        # For vowels
        elif char in vowels:
            if char == "ا" and i == 0:
                # Initial alif is silent
                continue
            # Index 0 gives the consonant version
            # Index 1 gives the voweled version
            if next_is_vowel:
                output_line.append(vowels[char][1])
                next_is_vowel = False
            else:
                output_line.append(vowels[char][0])
        elif (char in diphthongs and next_char and next_char in
                diphthongs[char]):
            next_is_diphthong = True
            output_line.append(diphthongs[char][next_char])
        # Only write the diacritic if the next char is not
        # its corresponding long vowel
        # if it is, skip it
        elif (char in diacritics and
                next_char and next_char in diacritics[char]):
            next_is_vowel = True
            continue
        else:
            mapped = mapping.get(char)
            if mapped:
                output_line.append(mapped)
            elif keep_unknown:
                output_line.append(char)
    output = seperator.join(output_line)
    return output


def main():
    args = argparser.parse_args()
    seperator = args.seperator
    keep_unknown = args.keep_unknown
    with open(INPUT_FILE, "r") as file:
        f = file.read()
        for line in f:
            output = "%s\n" % arabic_to_ipa(line, seperator=seperator,
                                            keep_unknown=keep_unknown)
            try:
                sys.stdout.write(output)
                with open(OUTPUT_FILE, 'a') as of:
                    of.write(output)
            except IOError:
                try:
                    sys.stdout.close()
                except IOError:
                    exit(1)
                try:
                    sys.stderr.close()
                except IOError:
                    exit(1)
                exit(0)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(
            description="Converts arabic strings into IPA phones naively.")
    argparser.add_argument('-s', '--seperator', type=str, default=" ",
                           help='What char to seperate IPA symbols with'
                           '(default: " ")')
    argparser.add_argument('-k', "--keep-unknown", default=True, action="store_true",
                           help='Keep unrecognized symbols that cannot be'
                           'turned to IPA')

    main()
