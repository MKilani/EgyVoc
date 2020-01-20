# -*- coding: utf-8 -*-

import copy


def parseCopticSahidic(lexicalItem, verbose=False):

    #add indicator beginning (#) / end ($) of word
    lexicalItem = "#" + lexicalItem + "$"

    copticForm = lexicalItem

    copticLetters = list(lexicalItem)

    translitLexicalItem = lexicalItem


    translitLexicalItem = translitLexicalItem.replace("ⲟⲩ", "ⲞⲨ")
    translitLexicalItem = translitLexicalItem.replace("ⲉⲓ", "ⲓ")
    #translitLexicalItem = translitLexicalItem.replace("ϯ", "ⲧⲓ")
    translitLexicalItem = translitLexicalItem.replace("ⲁⲓ", "a.j.")

    translitLexicalItem = translitLexicalItem.replace("ⲁⲁ", "a.ʔ.")
    translitLexicalItem = translitLexicalItem.replace("ⲉⲉ", "e.ʔ.")
    translitLexicalItem = translitLexicalItem.replace("ⲏⲏ", "ē.ʔ.")
    translitLexicalItem = translitLexicalItem.replace("ⲓⲓ", "ī.j.")
    translitLexicalItem = translitLexicalItem.replace("ⲟⲟ", "o.ʔ.")
    translitLexicalItem = translitLexicalItem.replace("ⲩⲩ", "u.ʔ.")
    translitLexicalItem = translitLexicalItem.replace("ⲱⲱ", "ō.ʔ.")
    translitLexicalItem = translitLexicalItem.replace("ʔ.ⲩ", "ʔ.w.")

    vowels = 0
    letters = list(translitLexicalItem)

    for letter in letters:
        if letter == u"ⲁ" \
                or letter == u"ⲉ" \
                or letter == u"ⲏ" \
                or letter == u"ⲓ" \
                or letter == u"ⲟ" \
                or letter == u"ⲩ" \
                or letter == u"ⲱ" \
                or letter == u"Ⲟ" \
                or letter == u"Ⲩ" \
                or letter == u"a" \
                or letter == u"e" \
                or letter == u"ē" \
                or letter == u"ī" \
                or letter == u"o" \
                or letter == u"u" \
                or letter == u"ō":
            vowels = vowels + 1

    if ("ⲱ" in translitLexicalItem \
            or "ⲟ" in translitLexicalItem \
            or "ⲏ" in translitLexicalItem \
            or "ϯ" in translitLexicalItem):
        translitLexicalItem = translitLexicalItem.replace("ⲞⲨ", "w.")
        translitLexicalItem = translitLexicalItem.replace("ⲩ", "w.")
        translitLexicalItem = translitLexicalItem.replace("ⲉ", "ə.")
        translitLexicalItem = translitLexicalItem.replace("ⲓ", "j.")
        translitLexicalItem = translitLexicalItem.replace("ⲁ", "ă.")

        translitLexicalItem = translitLexicalItem.replace("ⲱ", "ō.")
        translitLexicalItem = translitLexicalItem.replace("ⲟ", "o.")
        translitLexicalItem = translitLexicalItem.replace("ⲏ", "ē.")
        translitLexicalItem = translitLexicalItem.replace("ϯ$", "t.ɨ.")
        translitLexicalItem = translitLexicalItem.replace("ϯ", "t.ī.")

    elif ("ⲁⲩ" in translitLexicalItem):
        translitLexicalItem = translitLexicalItem.replace("ⲁⲩ", "a.w.")
    elif ("ⲉⲩ" in translitLexicalItem):
        translitLexicalItem = translitLexicalItem.replace("ⲉⲩ", "e.w.")
    elif ("ⲁ" in translitLexicalItem \
          and vowels == 1):
        translitLexicalItem = translitLexicalItem.replace("ⲁ", "a.")
    elif ("ⲓ" in translitLexicalItem \
          and vowels == 1):
        translitLexicalItem = translitLexicalItem.replace("ⲓ", "ī.")
    elif ("ⲉ" in translitLexicalItem \
          and vowels == 1):
        translitLexicalItem = translitLexicalItem.replace("ⲉ", "e.")
    elif ("ⲁ" in translitLexicalItem \
          and "ⲉ" in translitLexicalItem \
          and translitLexicalItem.find('ⲉ') < translitLexicalItem.find('ⲁ')):
        translitLexicalItem = translitLexicalItem.replace("ⲉ", "ə.")
        translitLexicalItem = translitLexicalItem.replace("ⲁ", "a.")
    elif ("ⲓ" in translitLexicalItem \
          and "ⲁ" in translitLexicalItem \
          and translitLexicalItem.find('ⲓ') < translitLexicalItem.find('ⲁ')):
        translitLexicalItem = translitLexicalItem.replace("ⲓ", "j.")
        translitLexicalItem = translitLexicalItem.replace("ⲁ", "a.")
    elif ("ⲞⲨ" in translitLexicalItem \
          and "ⲁ" in translitLexicalItem \
          and translitLexicalItem.find('Ⲟ') < translitLexicalItem.find('ⲁ')):
        translitLexicalItem = translitLexicalItem.replace("ⲞⲨ", "w.")
        translitLexicalItem = translitLexicalItem.replace("ⲁ", "a.")
    elif (translitLexicalItem.count("ⲁ")):
        translitLexicalItem = translitLexicalItem.replace("ⲁ", "ă.", 1)
        translitLexicalItem = translitLexicalItem.replace("ⲁ", "a.")

    translitLexicalItem = translitLexicalItem.replace("ⲁ", "ă|a.")
    translitLexicalItem = translitLexicalItem.replace("ⲉ", "ə|e.")
    translitLexicalItem = translitLexicalItem.replace("ⲓ", "j|ī.")
    translitLexicalItem = translitLexicalItem.replace("ⲞⲨ", "w|ū.")

    translitLexicalItem = translitLexicalItem.replace("ⲃ", "b.") \
        .replace("ⲅ", "g.") \
        .replace("ⲇ", "d.") \
        .replace("ⲋ", "s.") \
        .replace("ⲍ", "z.") \
        .replace("ⲑ", "tʰ.") \
        .replace("ⲕ", "k.") \
        .replace("ⲗ", "l.") \
        .replace("ⲙ", "m.") \
        .replace("ⲛ", "n.") \
        .replace("ⲝ", "k.s.") \
        .replace("ⲡ", "p.") \
        .replace("ⲣ", "r.") \
        .replace("ⲥ", "s.") \
        .replace("ⲧ", "t.") \
        .replace("ⲫ", "pʰ.") \
        .replace("ⲭ", "kʰ.") \
        .replace("ⲯ", "p.s.") \
        .replace("ϣ", "ʃ.") \
        .replace("ϥ", "f.") \
        .replace("ϧ", "x.") \
        .replace("ϩ", "h.") \
        .replace("ⳉ", "χ.") \
        .replace("ϫ", "c.") \
        .replace("ϭ", "kʲ.") \
        .replace("#", "#.")

    phonemes = translitLexicalItem.split(".")

    vowelCounter = 0
    consonatCounter = 0
    functionPhonCounter = 0

    for phoneme in phonemes:
        if ("ə" in phoneme or "ă" in phoneme or "a" in phoneme or "e" in phoneme
                or "o" in phoneme or "u" in phoneme or "ē" in phoneme
                or "ī" in phoneme or "ō" in phoneme or "ū" in phoneme):
            vowelCounter = vowelCounter + 1
        elif ("#" in phoneme or "$" in phoneme):
            functionPhonCounter = functionPhonCounter + 1
        else:
            consonatCounter = consonatCounter + 1


    for i in range(0, len(phonemes)):
        if i == 1 and phonemes[i] == "w|ū":
            phonemes[i] = "w"
            vowelCounter = vowelCounter - 1
            consonatCounter = consonatCounter + 1

        if phonemes[i] == "j|ī" and not isConsonant(phonemes[i + 1]) == "cons" \
                and not phonemes[i + 1] == "$":
            phonemes[i] = "j"
            vowelCounter = vowelCounter - 1
            consonatCounter = consonatCounter + 1

        if phonemes[i] == "j|ī" and isConsonant(phonemes[i + 1]) == "cons" \
                and isConsonant(phonemes[i - 1]) == "cons":
            phonemes[i] = "ī"
            for n in range(0, len(phonemes)):
                if "ə|e" in phonemes[n]:
                    phonemes[n] = "ə"

        if phonemes[i] == "ī":
            for n in range(0, len(phonemes)):
                if "ə|e" in phonemes[n]:
                    phonemes[n] = "ə"

        if phonemes[i] == "w|ū" and isConsonant(phonemes[i + 1]) == "cons" \
                and isConsonant(phonemes[i - 1]) == "cons":
            phonemes[i] = "ū"
            for n in range(0, len(phonemes)):
                if "ə|e" in phonemes[n]:
                    phonemes[n] = "ə"

        if "ə|e" in phonemes[i] and vowelCounter == 1:
            phonemes[i] = "e"
        if "ă|a" in phonemes[i] and vowelCounter == 1:
            phonemes[i] = "a"
        if "j|ī" in phonemes[i] and vowelCounter == 1:
            phonemes[i] = "ī"
        if "w|ū" in phonemes[i] and vowelCounter == 1:
            phonemes[i] = "ū"

    ###Sahidic
    if vowelCounter == 1 and phonemes[len(phonemes) - 2] == "e" and len(phonemes) > 4:
        phonemes.insert(2, "e")
        copticLetters.insert(2, "-")
        vowelCounter = vowelCounter + 1
        phonemes[len(phonemes) - 2] = "ə"

    glottalStop = False
    for i in range(0, len(phonemes)):
        if phonemes[i] == "ʔ":
            glottalStop = True
        if phonemes[i] == "ə|e" and glottalStop == True:
            phonemes[i] = "ə"

    shortA = False
    indexShortA = -1
    for i in range(0, len(phonemes)):
        if phonemes[i] == "ă" or phonemes[i] == "a":
            shortA = True
            indexShortA = i
        if phonemes[i] == "ə|e" and shortA == True:
            phonemes[i] = "ə"
            phonemes[indexShortA] = "a"

    ###Sahidic

    if vowelCounter > 1:
        if phonemes[len(phonemes) - 1] == "$" and phonemes[len(phonemes) - 2] == "j|ī":
            phonemes[len(phonemes) - 2] = "j"
            vowelCounter = vowelCounter - 1
            consonatCounter = consonatCounter + 1
            if vowelCounter == 1:
                for i in range(0, len(phonemes)):
                    if phonemes[i] == "ə|e":
                        phonemes[i] = "e"
                    if phonemes[i] == "ă":
                        phonemes[i] = "a"

    ###Bohairic
    # if vowelCounter > 1:
    #     if phonemes[len(phonemes)-1] == "$" and phonemes[len(phonemes)-2] == "j|ī":
    #         phonemes[len(phonemes)-2] = "ɨ"
    #
    #         if vowelCounter == 2:
    #             for i in range(0, len(phonemes)):
    #                 if phonemes[i] == "ə|e":
    #                     phonemes[i] = "e"
    #                 if phonemes[i] == "ă":
    #                     phonemes[i] = "a"

    if vowelCounter == 0:
        phonemes.insert(2, "e")
        copticLetters.insert(2, "-")
        vowelCounter = vowelCounter + 1

    phonemeClass = []

    for phoneme in phonemes:
        if ("j|ī" in phoneme or "w|ū" in phoneme):
            phonemeClass.append("W")
        elif ("ə" in phoneme or "ă" in phoneme or "a" in phoneme or "e" in phoneme
              or "o" in phoneme or "u" in phoneme or "ē" in phoneme
              or "ī" in phoneme or "ō" in phoneme or "ū" in phoneme):
            phonemeClass.append("V")
        elif ("#") in phoneme:
            phonemeClass.append("#")
        elif ("$") in phoneme:
            phonemeClass.append("$")
        else:
            phonemeClass.append("C")

    stressClass = []

    for phoneme in phonemes:
        if ("j|ī" in phoneme or "w|ū" in phoneme):
            stressClass.append("s")
        elif phoneme == "ə" or phoneme == "ă":
            stressClass.append("U")
        elif ("ə|" in phoneme or "ă|" in phoneme):
            stressClass.append("u")
        elif ("a" in phoneme or "e" in phoneme or "o" in phoneme or "u" in phoneme
              or "ē" in phoneme or "ī" in phoneme or "ō" in phoneme or "ū" in phoneme):
            stressClass.append("S")
        elif ("#") in phoneme:
            stressClass.append("#")
        elif ("$") in phoneme:
            stressClass.append("$")
        else:
            stressClass.append("0")

    lengthClass = []

    for phoneme in phonemes:
        if ("j|ī" in phoneme or "w|ū" in phoneme):
            lengthClass.append("l")
        elif phoneme == "ə" or phoneme == "ă":
            lengthClass.append("u")
        elif ("ə|" in phoneme or "ă|" in phoneme):
            lengthClass.append("s")
        elif ("a" in phoneme or "e" in phoneme or "o" in phoneme or "u" in phoneme):
            lengthClass.append("S")
        elif ("ē" in phoneme or "ī" in phoneme or "ō" in phoneme or "ū" in phoneme):
            lengthClass.append("L")
        elif ("#") in phoneme:
            lengthClass.append("#")
        elif ("$") in phoneme:
            lengthClass.append("$")
        else:
            lengthClass.append("0")


    #prepare results

    results = {}

    if verbose == True:
        print("Coptic form: " + copticForm.replace("#", "").replace("$", ""))
    results['CopticForm'] = copticForm.replace("#", "").replace("$", "")

    string = ""
    for item in phonemes:
        string = string + item + "."

    if verbose == True:
        print("Phonemes: " + string.replace("#.", "").replace(".$.", ""))
    results['Phonemes'] = string.replace("#.", "").replace(".$.", "")

    if verbose == True:
        print("Nr of vowels: " + str(vowelCounter))
        print("Nr of consonants: " + str(consonatCounter))
    results['NrVowels'] = vowelCounter
    results['NrConsonants'] = consonatCounter

    string = ""
    for item in phonemeClass:
        string = string + item + "."

    if verbose == True:
        print("Phoneme classes: " + string.replace("#.", "").replace(".$.", ""))
    results['PhonemeClasses'] = string.replace("#.", "").replace(".$.", "")

    string = ""
    for item in stressClass:
        string = string + item + "."

    if verbose == True:
        print("Stress: " + string.replace("#.", "").replace(".$.", ""))
    results['Stress'] = string.replace("#.", "").replace(".$.", "")

    string = ""
    for item in lengthClass:
        string = string + item + "."

    if verbose == True:
        print("Vowel Length: " + string.replace("#.", "").replace(".$.", ""))
    results['VowelLength'] = string.replace("#.", "").replace(".$.", "")

    return (results)



# function "is consonant?"

def isConsonant(phoneme):
    valCons = ""

    if phoneme == "b" \
            or phoneme == "g" \
            or phoneme == "d" \
            or phoneme == "s" \
            or phoneme == "z" \
            or phoneme == "tʰ" \
            or phoneme == "k" \
            or phoneme == "l" \
            or phoneme == "m" \
            or phoneme == "n" \
            or phoneme == "p" \
            or phoneme == "r" \
            or phoneme == "s" \
            or phoneme == "t" \
            or phoneme == "pʰ" \
            or phoneme == "kʰ" \
            or phoneme == "ʃ" \
            or phoneme == "f" \
            or phoneme == "x" \
            or phoneme == "h" \
            or phoneme == "c" \
            or phoneme == "kʲ" \
            or phoneme == "j" \
            or phoneme == "w":
        valCons = "cons"

        return valCons
