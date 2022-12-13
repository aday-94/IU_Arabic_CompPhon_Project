""" L645 ANLP Comp Phon Final Project Fall 2022 Andrew Davis -- Step 6: List of Regex for Removing Punctuation in Arabic Text -- Produces pre-Silver Standard  """

import re

IN = open('f2k22data-step5-arbipa-diacriticsipa-phone1-gem.txt', encoding = 'utf-8')
OUT = open('f2k22data-step6-arbipa-removedpunct-phone1-gem.txt', 'w')

text = IN.read()

def remove_punctuation(text):
    
    period = re.compile("\.", re.VERBOSE)
    exclam = re.compile("\!", re.VERBOSE)
    qmark = re.compile("\?", re.VERBOSE)
    uscore = re.compile("\_", re.VERBOSE)
    start_quote = re.compile("\"", re.VERBOSE)
    end_quote = re.compile("\"", re.VERBOSE)
    weird_quoteone = re.compile("\“", re.VERBOSE)
    weird_quotetwo = re.compile("\”", re.VERBOSE)
    one_quote = re.compile("\'", re.VERBOSE)
    colon = re.compile("\:", re.VERBOSE)
    d_left_arrow = re.compile("\«", re.VERBOSE)
    d_right_arrow = re.compile("\»", re.VERBOSE)
    slight_uscore = re.compile("\ـ", re.VERBOSE)
    dash = re.compile("\-", re.VERBOSE)
    semicolon = re.compile("\;", re.VERBOSE)
    comma = re.compile("\,", re.VERBOSE)
    arbqmark = re.compile("\؟", re.VERBOSE)
    arbcomma = re.compile("\،", re.VERBOSE)
    arb_semicolon_one = re.compile("\؛", re.VERBOSE)
    arb_semicolon_two = re.compile("\؛", re.VERBOSE)

    text = re.sub(period, "", text)
    text = re.sub(exclam, "", text)
    text = re.sub(qmark, "", text)
    text = re.sub(uscore, "", text)
    text = re.sub(start_quote, "", text)
    text = re.sub(end_quote, "", text)
    text = re.sub(weird_quoteone, "", text)
    text = re.sub(weird_quotetwo, "", text)
    text = re.sub(one_quote, "", text)
    text = re.sub(colon, "", text)
    text = re.sub(d_left_arrow, "", text)
    text = re.sub(d_right_arrow, "", text)
    text = re.sub(slight_uscore, "", text)
    text = re.sub(dash, "", text)
    text = re.sub(semicolon, "", text)
    text = re.sub(comma, "", text)
    text = re.sub(arbqmark, "", text)
    text = re.sub(arbcomma, "", text)
    text = re.sub(arb_semicolon_one, "", text)
    text = re.sub(arb_semicolon_two, "", text)

    return text

nopunct = remove_punctuation(text)

print(nopunct)

for w in nopunct:
    OUT.write(w)

IN.close()
OUT.close()