from ..dependencies.interfaceFAAL import interfaceFAAL

def joinCopticRoot (EgyptianRoot, parsedCoptic):

    CopticForm = parsedCoptic["CopticForm"]
    CopticPhonemes = parsedCoptic["Phonemes"].split(".")
    CopticPhonemeClasses = parsedCoptic["PhonemeClasses"].split(".")
    CopticStress = parsedCoptic["Stress"].split(".")
    CopticVowelLength = parsedCoptic["VowelLength"].split(".")

    CopticConsonats = extractConsonants(CopticPhonemeClasses, CopticPhonemes)

    EgyptianRootIPA = EgyptianRoot.replace("š", "ʃ")\
            .replace("ꜣ", "ʔ")\
            .replace("ꜥ", "ʕ")\
            .replace("ṯ", "c")\
            .replace("ḏ", "ɟ")\
            .replace("ẖ", "ç")\
            .replace("ḫ", "χ")\
            .replace("ḥ", "ħ")\
            .replace("y", "ɥ")

    

    consonantsAligned = interfaceFAAL(CopticConsonats, EgyptianRootIPA)

    indexConsonant = []

    for i in range(0, len(CopticPhonemeClasses)):
        if CopticPhonemeClasses[i] == "C":
            indexConsonant.append(i)


    CopticAligned = (("£" + consonantsAligned["wordWithoutDiacritics_1"] + "£").replace("┊", "").replace("￤", "").replace("£:", "").replace(":£", "")).split(":")
    RootAligned = (("£" + consonantsAligned["wordWithoutDiacritics_2"] + "£").replace("┊", "").replace("￤", "").replace("£:", "").replace(":£", "")).split(":")

    for i in range(0, len(CopticAligned)-1):
        if CopticAligned[i] == "0":
            if i < len(indexConsonant):
                CopticPhonemes.insert(indexConsonant[i], RootAligned[i])
                CopticPhonemeClasses.insert(indexConsonant[i], "C")
                CopticStress.insert(indexConsonant[i], "0")
                CopticVowelLength.insert(indexConsonant[i], "0")
            else:
                CopticPhonemes.append(RootAligned[i])
                CopticPhonemeClasses.append("C")
                CopticStress.append("0")
                CopticVowelLength.append("0")

            for n in range(i, len (indexConsonant)):
                indexConsonant[n] = indexConsonant[n]+1
            indexConsonant.insert(i, -1)

        else:
            if not RootAligned[i] == "0":
                CopticPhonemes[indexConsonant[i]] = RootAligned[i]

    if CopticAligned[-1] == "0":
        CopticPhonemes.append(RootAligned[i])
        CopticPhonemeClasses.append("C")
        CopticStress.append("0")
        CopticVowelLength.append("0")
    else:
        if not RootAligned[-1] == "0":
            if CopticPhonemeClasses[-1] == "C":
                CopticPhonemes[-1] = RootAligned[-1]
            if CopticPhonemeClasses[-1] == "V" and CopticPhonemeClasses[-2] == "C":
                CopticPhonemes[-2] = RootAligned[-1]

    results = {}

    results["CopticForm"] = CopticForm
    results["EgyptianRoot"] = EgyptianRoot
    results["PhonemesIPA"] = ".".join(CopticPhonemes)
    results["PhonemeClasses"] = ".".join(CopticPhonemeClasses)
    results["Stress"] = ".".join(CopticStress)
    results["VowelLength"] = ".".join(CopticVowelLength)

    results["Phonemes"] = results["PhonemesIPA"].replace("ʃ", "š")\
            .replace("ʔ", "ꜣ")\
            .replace("ʕ", "ꜥ")\
            .replace("c", "ṯ")\
            .replace("ɟ", "ḏ")\
            .replace("ç", "ẖ")\
            .replace("χ", "ḫ")\
            .replace("ħ", "ḥ")\
            .replace("ɥ", "y")

    return results


def joinReconstructions (parsedGroup, parsedCoptic, egyptianRoot = None):


    CopticPhonemes = parsedCoptic["Phonemes"].replace("ʃ", "š").split(".")
    CopticPhonemeClasses = parsedCoptic["PhonemeClasses"].split(".")
    CopticStress = parsedCoptic["Stress"].split(".")
    CopticVowelLength = parsedCoptic["VowelLength"].split(".")

    GroupPhonemes = parsedGroup["Phonemes"].split(".")
    GroupPhonemeClasses = parsedGroup["PhonemeClasses"].split(".")
    GroupStress = parsedGroup["Stress"].split(".")
    GroupVowelLength = parsedGroup["VowelLength"].split(".")

    CopticConsonantsIndex = []
    GroupConsonantsIndex = []

    indexConsonant = 0
    for letter in CopticStress:
        if letter == "0":
            CopticConsonantsIndex.append(indexConsonant)
            indexConsonant = indexConsonant + 1
        else:
            CopticConsonantsIndex.append("-")

    indexConsonant = 0
    for letter in GroupStress:
        if letter == "0":
            GroupConsonantsIndex.append(indexConsonant)
            indexConsonant = indexConsonant + 1
        else:
            GroupConsonantsIndex.append("-")


    CopticConsonats = extractConsonants(CopticPhonemeClasses, CopticPhonemes)

    GroupConsonats = extractConsonants(GroupPhonemeClasses, GroupPhonemes)

    consonantsAligned = interfaceFAAL(CopticConsonats, GroupConsonats)


    CopticAligned = (("£" + consonantsAligned["wordWithoutDiacritics_1"] + "£").replace("┊", "").replace("￤", "").replace("£:", "").replace(":£", "")).split(":")
    GroupAligned = (("£" + consonantsAligned["wordWithoutDiacritics_2"] + "£").replace("┊", "").replace("￤", "").replace("£:", "").replace(":£", "")).split(":")

    for i in range(0, len(CopticAligned)):
        if CopticAligned[i] == "0":
            found = False
            for n in range(0, len(CopticConsonantsIndex)):
                if CopticConsonantsIndex[n] == i:
                    #before the index, add cons + vowel0
                    CopticPhonemes.insert(n, "∅")
                    CopticPhonemes.insert(n, "⒞")

                    CopticPhonemeClasses.insert(n, "v")
                    CopticPhonemeClasses.insert(n, "C")

                    CopticStress.insert(n, "u")
                    CopticStress.insert(n, "0")

                    CopticVowelLength.insert(n, "u")
                    CopticVowelLength.insert(n, "0")

                    found = True
            if found == False:
                # append at the end

                CopticPhonemes.append("⒞")
                CopticPhonemes.append("∅")

                CopticPhonemeClasses.append("C")
                CopticPhonemeClasses.append("v")

                CopticStress.append("0")
                CopticStress.append("u")

                CopticVowelLength.append("0")
                CopticVowelLength.append("u")


    for i in range(0, len(GroupAligned)):
        if GroupAligned[i] == "0":
            found = False
            for n in range(0, len(GroupConsonantsIndex)):
                if GroupConsonantsIndex[n] == i:
                    #before the index, add cons + vowel0
                    GroupPhonemes.insert(n, "∅")
                    GroupPhonemes.insert(n, "⒞")

                    GroupPhonemeClasses.insert(n, "v")
                    GroupPhonemeClasses.insert(n, "C")

                    GroupStress.insert(n, "u")
                    GroupStress.insert(n, "0")

                    GroupVowelLength.insert(n, "u")
                    GroupVowelLength.insert(n, "0")

                    found = True
            if found == False:
                # append at the end

                GroupPhonemes.append("⒞")
                GroupPhonemes.append("∅")

                GroupPhonemeClasses.append("C")
                GroupPhonemeClasses.append("v")

                GroupStress.append("0")
                GroupStress.append("u")

                GroupVowelLength.append("0")
                GroupVowelLength.append("u")

    #insert no-vowels in Coptic

    for i in range(0, len(CopticVowelLength)-2):

        if CopticVowelLength[i] == "S" and CopticPhonemeClasses[i + 1] == "C" and CopticPhonemeClasses[i + 2] == "C":

            CopticPhonemes.insert(i+2, "⤫")
            CopticPhonemeClasses.insert(i+2, "⤫")
            CopticStress.insert(i+2, "⤫")
            CopticVowelLength.insert(i+2, "⤫")

    #insert possibly missing vowels in Coptic

    for i in range(0, len(CopticVowelLength) - 1):

        if CopticPhonemeClasses[i] == "C" and CopticPhonemeClasses[i + 1] == "C":
            CopticPhonemes.insert(i + 1, "∅")
            CopticPhonemeClasses.insert(i + 1, "v")
            CopticStress.insert(i + 1, "u")
            CopticVowelLength.insert(i + 1, "u")

    # insert no-vowels in Group Writing

    for i in range(0, len(GroupVowelLength) - 1):

        if GroupPhonemeClasses[i] == "C" and GroupPhonemeClasses[i + 1] == "C":
            GroupPhonemes.insert(i + 1, "⤫")
            GroupPhonemeClasses.insert(i + 1, "⤫")
            GroupStress.insert(i + 1, "⤫")
            GroupVowelLength.insert(i + 1, "⤫")


    # compare



    #print (CopticPhonemes)
    #print (CopticPhonemeClasses)
    #print (CopticStress)
    #print (CopticVowelLength)

    #print (GroupPhonemes)
    #print (GroupPhonemeClasses)
    #print (GroupStress)
    #print (GroupVowelLength)

    CombinedPhonemes = []
    CombinedPhonemeClasses = []
    CombinedStress = []
    CombinedVowelLength = []

    for i in range(0, len(CopticPhonemes)):
        if CopticPhonemeClasses[i] == "C" and GroupPhonemeClasses[i] == "C":
            if CopticPhonemes[i] == "⒞":
                CombinedPhonemes.append(GroupPhonemes[i])
                CombinedPhonemeClasses.append(GroupPhonemeClasses[i])
                CombinedStress.append(GroupStress[i])
                CombinedVowelLength.append(GroupVowelLength[i])
            elif GroupPhonemes[i] == "⒞":
                CombinedPhonemes.append(CopticPhonemes[i])
                CombinedPhonemeClasses.append(CopticPhonemeClasses[i])
                CombinedStress.append(CopticStress[i])
                CombinedVowelLength.append(CopticVowelLength[i])

            else:
                CombinedPhonemes.append(GroupPhonemes[i])
                CombinedPhonemeClasses.append(GroupPhonemeClasses[i])
                CombinedStress.append(GroupStress[i])
                CombinedVowelLength.append(GroupVowelLength[i])

        elif CopticPhonemeClasses[i] == "V" and GroupPhonemeClasses[i] == "V":
            if CopticPhonemes[i] in GroupPhonemes[i]:
                CombinedPhonemes.append(CopticPhonemes[i])
                CombinedPhonemeClasses.append(CopticPhonemeClasses[i])
                CombinedStress.append(CopticStress[i])
                CombinedVowelLength.append(CopticVowelLength[i])
            elif GroupPhonemes[i] in CopticPhonemes[i]:
                CombinedPhonemes.append(GroupPhonemes[i])
                CombinedPhonemeClasses.append(GroupPhonemes[i])
                CombinedStress.append(GroupPhonemes[i])
                CombinedVowelLength.append(GroupPhonemes[i])
            elif CopticPhonemes[i] == "ə" and GroupPhonemes[i] == "ŭ":
                CombinedPhonemes.append(GroupPhonemes[i])
                CombinedPhonemeClasses.append(GroupPhonemeClasses[i])
                CombinedStress.append(GroupStress[i])
                CombinedVowelLength.append(GroupVowelLength[i])
            else:
                CombinedPhonemes.append("?")
                CombinedPhonemeClasses.append("?")
                CombinedStress.append("?")
                CombinedVowelLength.append("?")

        elif CopticPhonemes[i] == "∅" and GroupPhonemes[i] == "∅":
            CombinedPhonemes.append("⤫")
            CombinedPhonemeClasses.append("⤫")
            CombinedStress.append("⤫")
            CombinedVowelLength.append("⤫")

        elif (CopticPhonemes[i] == "∅" and GroupPhonemes[i] == "⤫") or (CopticPhonemes[i] == "⤫" and GroupPhonemes[i] == "∅"):
            CombinedPhonemes.append("⤫")
            CombinedPhonemeClasses.append("⤫")
            CombinedStress.append("⤫")
            CombinedVowelLength.append("⤫")

        elif (CopticPhonemes[i] == "⤫" and "⤫" in GroupPhonemes[i]) or (GroupPhonemes[i] == "⤫" and "⤫" in CopticPhonemes[i]):
            CombinedPhonemes.append("⤫")
            CombinedPhonemeClasses.append("⤫")
            CombinedStress.append("⤫")
            CombinedVowelLength.append("⤫")

        elif not "⤫" in CopticPhonemes[i] and "⤫" in GroupPhonemes[i] and "|" in GroupPhonemes[i] and CopticPhonemes[i] in GroupPhonemes[i]:
            CombinedPhonemes.append(CopticPhonemes[i])
            CombinedPhonemeClasses.append(CopticPhonemes[i])
            CombinedStress.append(CopticPhonemes[i])
            CombinedVowelLength.append(CopticPhonemes[i])

        elif "|" in CopticPhonemes[i]:
            copticVowels = CopticPhonemes[i].split("|")
            matchVow = False
            for vowel in copticVowels:
                if vowel in GroupPhonemes[i]:
                    CombinedPhonemes.append(vowel)
                    CombinedPhonemeClasses.append("V")
                    CombinedStress.append("S")
                    if vowel == "ā" or vowel == "ī" or vowel == "ū" or vowel == "ē" or vowel == "ō":
                        CombinedVowelLength.append("L")
                    else:
                        CombinedVowelLength.append("S")
                    matchVow = True
            if matchVow == False:
                CombinedPhonemes.append("?")
                CombinedPhonemeClasses.append("?")
                CombinedStress.append("?")
                CombinedVowelLength.append("?")
        else:
            CombinedPhonemes.append("?")
            CombinedPhonemeClasses.append("?")
            CombinedStress.append("?")
            CombinedVowelLength.append("?")

    results = {}

    results["Phonemes"] = ".".join(CombinedPhonemes)
    results["PhonemesIPA"] = results["Phonemes"].replace("š", "ʃ")\
            .replace("ꜣ", "ʔ")\
            .replace("ꜥ", "ʕ")\
            .replace("ṯ", "c")\
            .replace("ḏ", "ɟ")\
            .replace("ẖ", "ç")\
            .replace("ḫ", "χ")\
            .replace("ḥ", "ħ")\
            .replace("y", "ɥ")
    results["PhonemeClasses"] = ".".join(CombinedPhonemeClasses)
    results["Stress"] = ".".join(CombinedStress)
    results["VowelLength"] = ".".join(CombinedVowelLength)

    return results











def extractConsonants(classes, phonemes):
    consonants = ""
    for i in range(0, len(classes)):
        if classes[i] == "C":
            consonants = consonants + phonemes[i]

            consonants = consonants.replace("š", "ʃ")\
            .replace("ꜣ", "ʔ")\
            .replace("ꜥ", "ʕ")\
            .replace("ṯ", "c")\
            .replace("ḏ", "ɟ")\
            .replace("ẖ", "ç")\
            .replace("ḫ", "χ")\
            .replace("ḥ", "ħ")\
            .replace("y", "ɥ")


    return consonants


