""" L645 ANLP Comp Phon Final Project Fall 2022 Andrew Davis -- Step 5: List of Regex for Diacritic Transcription in Arabic Text ; See Wikipedia for Arabic Diacritics """

import re

IN = open('f2k22data-step4-arbipa-eng&oddrem-phon1-gem.txt', encoding = 'utf-8')
OUT = open('f2k22data-step5-arbipa-diacriticsipa-phone1-gem.txt', 'w')

text = IN.read()

""" Arabic Diacritic Character Conversion to IPA """

def arab_diacritics_ipa(text):

    fatha = re.compile("""َ""", re.VERBOSE)
    kasrah = re.compile("""ِ""", re.VERBOSE)
    dammah = re.compile("""ُ""", re.VERBOSE)
    daggeralif = re.compile("""ٰ""", re.VERBOSE)
    #alifwaslah = re.compile("ٱ", re.VERBOSE) PUT THESE THREE ALIFS IN CONSONANTS
    #alifmaddah = re.compile("آ", re.VERBOSE)
    #alifmaqsurah = re.compile("ى", re.VERBOSE)
    #flexiblealif = re.compile()
    sukun = re.compile("""ْ""", re.VERBOSE)
    tanwin_un = re.compile(" ٌ", re.VERBOSE)
    tanwin_in = re.compile("""ٍ""", re.VERBOSE)
    tanwin_an = re.compile("""ً""", re.VERBOSE)
    shaddah = re.compile("""ّ""", re.VERBOSE)
    hamza = re.compile("ء", re.VERBOSE)
    #hamzaupchair = re.compile("أ", re.VERBOSE) PUT THESE TWO CHAIRS IN CONSONANTS
    #hamzadownchair = re.compile("إ", re.VERBOSE)
    #yehamza = re.compile("ئ", re.VERBOSE) PUT THESE TWO HAMZA WAW YA'S IN CONSONANTS
    #wawhamza = re.compile("ؤ", re.VERBOSE)
    tamarbuta = re.compile("ة", re.VERBOSE)
    #la = re.compile("ﻻ", re.VERBOSE) #will add this to consonants eventually

    text = re.sub(fatha, 'a', text)
    text = re.sub(kasrah, 'i', text)
    text = re.sub(dammah, 'u', text)
    text = re.sub(daggeralif, 'aː', text)
    #text = re.sub(alifwaslah, 'aː', text)
    #text = re.sub(alifmaddah, 'ʔaː', text)
    #text = re.sub(alifmaqsurah, 'aː', text)
    text = re.sub(sukun, '', text)
    text = re.sub(tanwin_un, 'un', text)
    text = re.sub(tanwin_in, 'in', text)
    text = re.sub(tanwin_an, 'an', text)
    text = re.sub(shaddah, '', text)
    text = re.sub(hamza, 'ʔ', text)
    #text = re.sub(hamzaupchair, 'ʔa', text)
    #text = re.sub(hamzadownchair, 'ʔi', text)
    #text = re.sub(yehamza, 'ʔi', text)
    #text = re.sub(wawhamza, 'ʔu', text)
    text = re.sub(tamarbuta, 'a', text)
    #text = re.sub(la, 'laː', text)

    return text

print(arab_diacritics_ipa(text))

diatext = arab_diacritics_ipa(text)

for w in diatext:
    OUT.write(w)

IN.close()
OUT.close()

""" Harakat (short vowel marks)

The ḥarakāt حَرَكَات, which literally means 'motions', are the short vowel marks. There is some ambiguity as to which tashkīl are also ḥarakāt; the tanwīn, for example, are markers for both vowels and consonants.
Fatḥah
ـَ‎

The fatḥah ⟨فَتْحَة⟩ is a small diagonal line placed above a letter, and represents a short /a/ (like the /a/ sound in the English word "cat"). The word fatḥah itself (فَتْحَة) means opening and refers to the opening of the mouth when producing an /a/. For example, with dāl (henceforth, the base consonant in the following examples): ⟨دَ⟩ /da/.

When a fatḥah is placed before a plain letter ⟨ا⟩ (alif) (i.e. one having no hamza or vowel of its own), it represents a long /aː/ (close to the sound of "a" in the English word "dad", with an open front vowel /æː/, not back /ɑː/ as in "father"). For example: ⟨دَا⟩ /daː/. The fatḥah is not usually written in such cases. When a fathah placed before the letter ⟨ﻱ⟩ (yā’), it creates an /aj/ (as in "lie"); and when placed before the letter ⟨و⟩ (wāw), it creates an /aw/ (as in "cow").

Although paired with a plain letter creates an open front vowel (/a/), often realized as near-open (/æ/), the standard also allows for variations, especially under certain surrounding conditions. Usually, in order to have the more central (/ä/) or back (/ɑ/) pronunciation, the word features a nearby back consonant, such as the emphatics, as well as qāf, or rā’. A similar "back" quality is undergone by other vowels as well in the presence of such consonants, however not as drastically realized as in the case of fatḥah.[1][2][3]
Kasrah
ـِ‎

A similar diagonal line below a letter is called a kasrah ⟨كَسْرَة⟩ and designates a short /i/ (as in "me", "be") and its allophones [i, ɪ, e, e̞, ɛ] (as in "Tim", "sit"). For example: ⟨دِ⟩ /di/.[4]

When a kasrah is placed before a plain letter ⟨ﻱ⟩ (yā’), it represents a long /iː/ (as in the English word "steed"). For example: ⟨دِي⟩ /diː/. The kasrah is usually not written in such cases, but if yā’ is pronounced as a diphthong /aj/, fatḥah should be written on the preceding consonant to avoid mispronunciation. The word kasrah means 'breaking'.[1]
Ḍammah
ـُ‎

The ḍammah ⟨ضَمَّة⟩ is a small curl-like diacritic placed above a letter to represent a short /u/ (as in "duke", shorter "you") and its allophones [u, ʊ, o, o̞, ɔ] (as in "put", or "bull"). For example: ⟨دُ⟩ /du/.[4]

When a ḍammah is placed before a plain letter ⟨و⟩ (wāw), it represents a long /uː/ (like the 'oo' sound in the English word "swoop"). For example: ⟨دُو⟩ /duː/. The ḍammah is usually not written in such cases, but if wāw is pronounced as a diphthong /aw/, fatḥah should be written on the preceding consonant to avoid mispronunciation.[1]

The word ḍammah (ضَمَّة) in this context means rounding, since it is the only rounded vowel in the vowel inventory of Arabic.
Alif Khanjariyah
ــٰ‎

The superscript (or dagger) alif ⟨أَلِف خَنْجَرِيَّة⟩ (alif khanjarīyah), is written as short vertical stroke on top of a consonant. It indicates a long /aː/ sound for which alif is normally not written. For example: ⟨هَٰذَا⟩ (hādhā) or ⟨رَحْمَٰن⟩ (raḥmān).

The dagger alif occurs in only a few words, but they include some common ones; it is seldom written, however, even in fully vocalised texts. Most keyboards do not have dagger alif. The word Allah ⟨الله⟩ (Allāh) is usually produced automatically by entering alif lām lām hāʾ. The word consists of alif + ligature of doubled lām with a shaddah and a dagger alif above lām.
Maddah
Not to be confused with Tilde.
ـٓ‎ آ ‎

The maddah ⟨مَدَّة⟩ is a tilde-shaped diacritic, which can only appear on top of an alif (آ) and indicates a glottal stop /ʔ/ followed by a long /aː/.

In theory, the same sequence /ʔaː/ could also be represented by two alifs, as in *⟨أَا⟩, where a hamza above the first alif represents the /ʔ/ while the second alif represents the /aː/. However, consecutive alifs are never used in the Arabic orthography. Instead, this sequence must always be written as a single alif with a maddah above it, the combination known as an alif maddah. For example: ⟨قُرْآن⟩ /qurˈʔaːn/.
Alif waslah
Main article: Wasla (diacritic)
ٱ‎

The waṣlah ⟨وَصْلَة⟩, alif waṣlah ⟨أَلِف وَصْلَة⟩ or hamzat waṣl ⟨هَمْزَة وَصْل⟩ looks like a small letter ṣād on top of an alif ⟨ٱ⟩ (also indicated by an alif ⟨ا⟩ without a hamzah). It means that the alif is not pronounced when its word does not begin a sentence. For example: ⟨بِٱسْمِ⟩ (bismi), but ⟨ٱمْشُوا۟⟩ (imshū not mshū). This is because no Arab word can start with a vowel-less consonant (unlike the English school, or skateboard). But when it happens, an alif is added to obtain a vowel or a vowelled consonant at the beginning of one's speech. In English that would result in *ischool, or *iskateboard.

It occurs only in the beginning of words, but it can occur after prepositions and the definite article. It is commonly found in imperative verbs, the perfective aspect of verb stems VII to X and their verbal nouns (maṣdar). The alif of the definite article is considered a waṣlah.

It occurs in phrases and sentences (connected speech, not isolated/dictionary forms):

    To replace the elided hamza whose alif-seat has assimilated to the previous vowel. For example: فِي ٱلْيَمَن or في اليمن (fi l-Yaman) ‘in Yemen’.
    In hamza-initial imperative forms following a vowel, especially following the conjunction ⟨و⟩ (wa-) ‘and’. For example: َقُمْ وَٱشْرَبِ ٱلْمَاءَ (qum wa-shrab-i l-mā’) ‘rise and then drink the water’.

Like the superscript alif, it is not written in fully vocalized scripts, except for sacred texts, like the Quran and Arabized Bible.
Sukūn
ـْـ‎

The sukūn ⟨سُكُونْ⟩ is a circle-shaped diacritic placed above a letter ( ْ). It indicates that the consonant to which it is attached is not followed by a vowel, i.e., zero-vowel.

It is a necessary symbol for writing consonant-vowel-consonant syllables, which are very common in Arabic. For example: ⟨دَدْ⟩ (dad).

The sukūn may also be used to help represent a diphthong. A fatḥah followed by the letter ⟨ﻱ⟩ (yā’) with a sukūn over it (ـَيْ) indicates the diphthong ay (IPA /aj/). A fatḥah, followed by the letter ⟨ﻭ⟩ (wāw) with a sukūn, (ـَوْ) indicates /aw/.
ـۡـ‎

The sukūn may have also an alternative form of the small high head of ḥāʾ (U+06E1 ۡ ), particularly in some Qurans. Other shapes may exist as well (for example, like a small comma above ⟨ʼ⟩ or like a circumflex ⟨ˆ⟩ in nastaʿlīq).[5]

Tanwin (final postnasalized or long vowels)
Main article: Nunation
ـٌ‎  ـٍ‎  ـً‎

The three vowel diacritics may be doubled at the end of a word to indicate that the vowel is followed by the consonant n. They may or may not be considered ḥarakāt and are known as tanwīn ⟨تَنْوِين⟩, or nunation. The signs indicate, from left to right, -un, -in, -an.

These endings are used as non-pausal grammatical indefinite case endings in Literary Arabic or classical Arabic (triptotes only). In a vocalised text, they may be written even if they are not pronounced (see pausa). See i‘rāb for more details. In many spoken Arabic dialects, the endings are absent. Many Arabic textbooks introduce standard Arabic without these endings. The grammatical endings may not be written in some vocalized Arabic texts, as knowledge of i‘rāb varies from country to country, and there is a trend towards simplifying Arabic grammar.

The sign ⟨ـً⟩ is most commonly written in combination with ⟨ـًا⟩ (alif), ⟨ةً⟩ (tā’ marbūṭah), ⟨أً⟩ (alif hamzah) or stand-alone ⟨ءً⟩ (hamzah). Alif should always be written (except for words ending in tā’ marbūṭah, hamzah or diptotes) even if an is not. Grammatical cases and tanwīn endings in indefinite triptote forms:

    -un: nominative case;
    -an: accusative case, also serves as an adverbial marker;
    -in: genitive case.

Shaddah (consonant gemination mark)
Main article: Shadda
ـّـ‎

The shadda or shaddah ⟨شَدَّة⟩ (shaddah), or tashdid ⟨تَشْدِيد⟩ (tashdīd), is a diacritic shaped like a small written Latin "w".

It is used to indicate gemination (consonant doubling or extra length), which is phonemic in Arabic. It is written above the consonant which is to be doubled. It is the only ḥarakah that is commonly used in ordinary spelling to avoid ambiguity. For example: ⟨دّ⟩ /dd/; madrasah ⟨مَدْرَسَة⟩ ('school') vs. mudarrisah ⟨مُدَرِّسَة⟩ ('teacher', female). 

Although normally a diacritic is not considered a letter of the alphabet, the hamza هَمْزة (hamzah, glottal stop), often stands as a separate letter in writing, is written in unpointed texts and is not considered a tashkīl. It may appear as a letter by itself or as a diacritic over or under an alif, wāw, or yā.

Which letter is to be used to support the hamzah depends on the quality of the adjacent vowels;

    If the glottal stop occurs at the beginning of the word, it is always indicated by hamza on an alif: above if the following vowel is /a/ or /u/ and below if it is /i/.
    If the glottal stop occurs in the middle of the word, hamzah above alif is used only if it is not preceded or followed by /i/ or /u/:
        If /i/ is before or after the glottal stop, a yāʼ with a hamzah is used (the two dots which are usually beneath the yāʾ disappear in this case): ⟨ئ⟩.
        Otherwise, if /u/ is before or after the glottal stop, a wāw with a hamzah is used: ⟨ؤ⟩.
    If the glottal stop occurs at the end of the word (ignoring any grammatical suffixes), if it follows a short vowel it is written above alif, wāw, or yā the same as for a medial case; otherwise on the line (i.e. if it follows a long vowel, diphthong or consonant).
    Two alifs in succession are never allowed: /ʔaː/ is written with alif maddah ⟨آ⟩ and /aːʔ/ is written with a free hamzah on the line ⟨اء⟩.

Consider the following words: ⟨أَخ⟩ /ʔax/ ("brother"), ⟨إسْماعِيل⟩ /ʔismaːʕiːl/ ("Ismael"), ⟨أُمّ⟩ /ʔumm/ ("mother"). All three of above words "begin" with a vowel opening the syllable, and in each case, alif is used to designate the initial glottal stop (the actual beginning). But if we consider middle syllables "beginning" with a vowel: ⟨نَشْأة⟩ /naʃʔa/ ("origin"), ⟨أَفْئِدة⟩ /ʔafʔida/ ("hearts"—notice the /ʔi/ syllable; singular ⟨فُؤاد⟩ /fuʔaːd/), ⟨رُؤُوس⟩ /ruʔuːs/ ("heads", singular ⟨رَأْس⟩ /raʔs/), the situation is different, as noted above. See the comprehensive article on hamzah for more details. 
 """