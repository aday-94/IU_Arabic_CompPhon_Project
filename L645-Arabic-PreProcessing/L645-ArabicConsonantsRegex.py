""" L645 ANLP Comp Phon Final Project Fall 2022 Andrew Davis -- Step 4: List of Regex for Phoneme Transcription in Arabic Text ; See Wikipedia for Arabic Phonemes: https://en.wikipedia.org/wiki/Arabic_script_in_Unicode  """

import re

IN = open('f2k22data-step3-arbortho-eng&oddrem-phon1-gem.txt', encoding = 'utf-8')
OUT = open('f2k22data-step4-arbipa-eng&oddrem-phon1-gem.txt', 'w')

text = IN.read()

""" Arabic Phoneme Character Conversion to IPA """

def arab_characters_ipa(text):

    alifwaslah = re.compile("ٱ", re.VERBOSE)
    alifmaddah = re.compile("آ", re.VERBOSE)
    alifmaqsurah = re.compile("ى", re.VERBOSE)
    hamzaupchair = re.compile("أ", re.VERBOSE)
    hamzaupchair_b = re.compile("ﺃ", re.VERBOSE)
    hamzadownchair = re.compile("إ", re.VERBOSE)
    alif = re.compile("ا", re.VERBOSE)

    ba = re.compile("ب", re.VERBOSE)
    ta = re.compile("ت", re.VERBOSE)
    tha = re.compile("ث", re.VERBOSE)
    jim = re.compile("ج", re.VERBOSE)
    ha_phar = re.compile ("ح", re.VERBOSE)
    kha = re.compile("خ", re.VERBOSE)
    dal = re.compile("د", re.VERBOSE)
    dhal = re.compile("ذ", re.VERBOSE)
    ra = re.compile("ر", re.VERBOSE)
    za = re.compile("ز", re.VERBOSE)
    sin = re.compile("س", re.VERBOSE)
    shin = re.compile("ش", re.VERBOSE)
    sad = re.compile("ص", re.VERBOSE)
    dad = re.compile("ض", re.VERBOSE)
    ta_emphatic = re.compile("ط", re.VERBOSE)
    tha_emphatic = re.compile("ظ", re.VERBOSE)
    ayn = re.compile("ع", re.VERBOSE)
    ghayn = re.compile("غ", re.VERBOSE)
    fa = re.compile("ف", re.VERBOSE)
    
    chechen_qaf = re.compile("ڨ", re.VERBOSE)
    qaf = re.compile("ق", re.VERBOSE)
    kaf = re.compile("ك", re.VERBOSE)

    la = re.compile("ﻻ", re.VERBOSE)
    lam = re.compile("ل", re.VERBOSE)

    mim = re.compile("م", re.VERBOSE)
    nun = re.compile("ن", re.VERBOSE)

    ha_doach = re.compile("ھ", re.VERBOSE)
    ha = re.compile("ه", re.VERBOSE)

    waw_hamza = re.compile("ؤ", re.VERBOSE)
    waw_uu = re.compile("ـُو", re.VERBOSE)
    waw_aw = re.compile("ـَو", re.VERBOSE)
    waw = re.compile("و", re.VERBOSE)
    
    ya_hamza = re.compile("ئ", re.VERBOSE)
    ya_ii = re.compile("ـِي", re.VERBOSE)
    ya_aj = re.compile("ـَي", re.VERBOSE)
    ya = re.compile("ي", re.VERBOSE)

    text = re.sub(alifwaslah, 'aː', text)
    text = re.sub(alifmaddah, 'ʔaː', text)
    text = re.sub(alifmaqsurah, 'aː', text)
    text = re.sub(hamzaupchair, 'ʔa', text)
    text = re.sub(hamzaupchair_b, 'ʔa', text)
    text = re.sub(hamzadownchair, 'ʔi', text)
    text = re.sub(alif, "aː", text)

    text = re.sub(ba, "b", text)
    text = re.sub(ta, "t", text)
    text = re.sub(tha, "θ", text)
    text = re.sub(jim, "d͡ʒ", text)
    text = re.sub(ha_phar, "ħ", text)
    text = re.sub(kha, "χ", text)
    text = re.sub(dal, "d", text)
    text = re.sub(dhal, "ð", text)
    text = re.sub(ra, "r", text)
    text = re.sub(za, "z", text)
    text = re.sub(sin, "s", text)
    text = re.sub(shin, "ʃ", text)
    text = re.sub(sad, "sˤ", text)
    text = re.sub(dad, "dˤ", text)
    text = re.sub(ta_emphatic, "tˤ", text)
    text = re.sub(tha_emphatic, "ðˤ", text)
    text = re.sub(ayn, "ʕ", text)
    text = re.sub(ghayn, "ʁ", text)
    text = re.sub(fa, "f", text)
    
    text = re.sub(chechen_qaf, "q", text)
    text = re.sub(qaf, "q", text)
    text = re.sub(kaf, "k", text)

    text = re.sub(la, 'laː', text)
    text = re.sub(lam, "l", text)

    text = re.sub(mim, "m", text)
    text = re.sub(nun, "n", text)

    text = re.sub(ha_doach, "h", text)
    text = re.sub(ha, "h", text)
    
    text = re.sub(waw_hamza, 'ʔu', text)
    text = re.sub(waw_uu, "uː", text)
    text = re.sub(waw_aw, "aw", text)
    text = re.sub(waw, "w", text)
    
    text = re.sub(ya_hamza, 'ʔi', text)
    text = re.sub(ya_ii, "iː", text)
    text = re.sub(ya_aj, "aj", text)
    text = re.sub(ya, "j", text)
    
    return text

print(arab_characters_ipa(text))

ipa_text = arab_characters_ipa(text)

for w in ipa_text:
    OUT.write(w)

IN.close()
OUT.close()