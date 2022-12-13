import re

IN = open('f2k22data-arbipa-diacritic-ipa.txt', encoding = 'utf-8')
OUT = open('f2k22data-arbipa-processed.txt', 'w')

text = IN.read()

words = text.split()

def shaddah_gem(words):
    
    shaddah = re.compile("""ّ""", re.VERBOSE)
    new_words = []

    for word in words:
        new_word = ''

        if shaddah.findall(word):
            
            shaddah_index = word.index(shaddah)
            gem = word

            word.insert(shaddah_index-1)
            """ for index, c in enumerate(word):
                if c == shaddah:
                    new_word += word[index-1]
                else:
                    new_word += c """
        
        else:
            new_word = word

        new_words.append(new_word + " ")
        
    print(new_word, word)
    return new_words

print(shaddah_gem(words))
            
    