# -*- coding: utf-8 -*-


def parseGroupWriting_2(lexicalItem):

    #add indicator beginning (#) / end ($) of word

    lexicalItem = "#." + lexicalItem + ".$"
    lexicalItem = lexicalItem.replace("#.#", "#.").replace("$.$", ".$")

    groupsRaw = lexicalItem.split(".")

    itemCleaned = ""

    # ] = no vowel after group CVC
    # 0 = single consonant group

    for group in groupsRaw:
        newGroup = group

        if len(newGroup) == 1 and "#" not in newGroup and "$" not in newGroup:
            newGroup = newGroup #+ "A"

        if len(newGroup) == 2 and "ʸ" in newGroup and "r" not in newGroup and "d" not in newGroup:
            newGroup = newGroup #+ "A"

        if newGroup == "rʸ":
            newGroup = "rʸ-"

        if len(newGroup) == 2 and not ("A" in newGroup) and not ("U" in newGroup) and not ("ʸ" in newGroup) and not ("-" in newGroup):
            newGroup = newGroup[0] + "A." + newGroup[1] + "]"

        if len(newGroup) > 2 and not ("ʸ" in newGroup):
            if len(newGroup) == 3 and newGroup[1] == "A":
                newGroup = newGroup[0] + newGroup[1] + "." + newGroup[2] + "]"


            if len(newGroup) == 3 and newGroup[2] == "U":
                newGroup = "[" + newGroup[0] + "U." + newGroup[1] + "]"

            if len(newGroup) == 4 and newGroup[3] == "U":
                newGroup = "[" + newGroup[0] + "U." + newGroup[2] + "]"

        itemCleaned = itemCleaned + newGroup + "."

    itemCleaned = itemCleaned.replace(".$.", ".$")

    groups = itemCleaned.split(".")

    parsedLexicalItem = []

    # group
    # cons
    # vowelClass
    # vowelHistorical
    # group or single consonant (len>1 / len1)
    # presence of y or not (+ʸ / -ʸ)

    # position of the vowel

    transcription = []
    consGroup = []
    consGroupIPA = []
    vocGroup = []
    vocGroupEdit = []
    vocGroupRec = []
    IDVowel = []

    IDVowel_nr = 0

    for group in groups:



        if group == "#":
            transcription.append("#")
            consGroup.append("#")
            consGroupIPA.append("#")
            vocGroup.append("#")
            vocGroupEdit.append("#")
            vocGroupRec.append("#")
            IDVowel.append("#")

        elif group == "$":
            if consGroup[-1] == "ʳ":
                consGroup[-1] = "r"
                vocGroup[-1] = "⤫"
                vocGroupEdit[-1] = "⤫"
                vocGroupRec[-1] = "|⤫"
                IDVowel[-1] = "-"

            transcription.append("$")
            consGroup.append("$")
            consGroupIPA.append("$")
            vocGroup.append("$")
            vocGroupEdit.append("$")
            vocGroupRec.append("$")
            IDVowel.append("$")

        elif ("kA" in group):
            #print("kA: " + group)

            transcription.append(group)
            consGroup.append(group.replace("A", ""))
            consGroupIPA.append(group.replace("A", ""))
            vocGroup.append("Ɔ")
            vocGroupEdit.append("Ɔ")
            vocGroupRec.append("|o|ō|u|ū")
            IDVowel.append(IDVowel_nr)
            IDVowel_nr = IDVowel_nr + 1

        elif ("kU" in group):
            #print("kU: " + group)

            transcription.append(group)
            consGroup.append(group.replace("U", ""))
            consGroupIPA.append(group.replace("U", ""))
            vocGroup.append("Ɔ")
            vocGroupEdit.append("Ɔ")
            vocGroupRec.append("|o|ō")
            IDVowel.append(IDVowel_nr)
            IDVowel_nr = IDVowel_nr + 1

        elif ("dʸ" in group):
            #print("dʸ: " + group)

            transcription.append(group)
            consGroup.append(group.replace("ʸ", ""))
            consGroupIPA.append(group.replace("ʸ", ""))
            vocGroup.append("U")
            vocGroupEdit.append("U")
            vocGroupRec.append("|u|ū|ō")
            IDVowel.append(IDVowel_nr)
            IDVowel_nr = IDVowel_nr + 1

        elif ("ḫʸ" in group):
            #print("ḫʸ: " + group)

            transcription.append(group)
            consGroup.append(group.replace("ʸ", ""))
            consGroupIPA.append(group.replace("ȟ", ""))
            vocGroup.append("A")
            vocGroupEdit.append("A")
            vocGroupRec.append("|a|i|ī|0")
            IDVowel.append(IDVowel_nr)
            IDVowel_nr = IDVowel_nr + 1

        elif ("ʸr" in group):
            #print("ʸr: " + group)

            transcription.append(group)
            consGroup.append("ʳ")
            consGroupIPA.append("r")
            vocGroup.append("-")
            vocGroupEdit.append("-")
            vocGroupRec.append("-")

            if len(vocGroupRec) > 1:
                vocGroupRec[-2] = vocGroupRec[-2].replace("|ā", "").replace("|ī", "").replace("|ū", "").replace("|ō",
                                                                                                                "")

            IDVowel.append("-")

        elif ("n-" in group):
            #print("n-: " + group)

            transcription.append(group)
            consGroup.append("ⁿ")
            consGroupIPA.append("ⁿ")
            vocGroup.append("ⁿ")
            vocGroupEdit.append("ⁿ")
            vocGroupRec.append("ⁿ")


        elif "]" in group:
            transcription.append(group)
            consGroup.append(group.replace("]", ""))
            consGroupIPA.append(group.replace("]", ""))
            vocGroup.append("⤫")
            vocGroupEdit.append("⤫]")
            vocGroupRec.append("|⤫|]")

        elif group == "":
            transcription.append("")
            consGroup.append("")
            consGroupIPA.append("")
            vocGroup.append("")
            vocGroupEdit.append("")
            vocGroupRec.append("")
            IDVowel.append("")
        else:

            group = group.replace("ʸ", "A")

            transcription.append(group)
            consGroup.append(transcription[-1].replace("A","").replace("U",""))
            consGroupIPA.append(transcription[-1].replace("A","").replace("U",""))
            if "A" in group:
                vocGroup.append("A")
                vocGroupEdit.append("A")
                vocGroupRec.append("|a|i|ī|0")
                IDVowel.append(IDVowel_nr)
                IDVowel_nr = IDVowel_nr + 1
            else:
                vocGroup.append("U")
                vocGroupEdit.append("U")
                vocGroupRec.append("|u|ū|ō")
                IDVowel.append(IDVowel_nr)
                IDVowel_nr = IDVowel_nr + 1


    i = 0
    while i < len(groups):
        if "ⁿ" in consGroup[i]:
            transcription[i+1] = "n-" + transcription[i+1]
            consGroup[i+1] = "ⁿ" + consGroup[i+1]
            consGroupIPA[i+1] = "ⁿ" + consGroupIPA[i+1]
            consGroupIPA[i + 1] = consGroupIPA[i+1].replace("ⁿr", "l")

            groups.pop(i)
            transcription.pop(i)
            consGroup.pop(i)
            consGroupIPA.pop(i)
            vocGroup.pop(i)
            vocGroupEdit.pop(i)
            vocGroupRec.pop(i)
            IDVowel.pop(i)
        i = i +1


    for i in range(0, len(groups)):
        if "[" in transcription[i]:
            consGroup[i] = consGroup[i].replace("[", "")
            consGroupIPA[i] = consGroupIPA[i].replace("[", "")
            vocGroupEdit[i] = "[" + vocGroupEdit[i]
            vocGroupRec[i] = "|[" + vocGroupRec[i]


    for i in range(1, len(groups)):

        if transcription[i-1] == transcription[i] and vocGroup[i] == "U":
            vocGroupRec[i - 1] = "|[" + vocGroupRec[i - 1]
            vocGroupRec[i] = "|]" + vocGroupRec[i]
            vocGroupEdit[i - 1] = vocGroupEdit[i - 1] + "]"
            vocGroupEdit[i] = "]" + vocGroupEdit[i]


        if consGroup[i-1] == "ʳ":
            vocGroup[i-1] = vocGroup[i]
            vocGroupRec[i-1] = "|>" + vocGroupRec[i]
            vocGroupRec[i] = "|<" + vocGroupRec[i]
            vocGroupEdit[i - 1] = vocGroupEdit[i] + ">"
            vocGroupEdit[i] = "<" + vocGroupEdit[i]
            vocGroupRec[i - 1] = vocGroupRec[i - 1].replace("|ū", "").replace("|ā", "").replace("|ī", "").replace("|ō",
                                                                                                                  "")

            IDVowel[i - 1] = IDVowel[i]

        if "|⤫|]" in vocGroupRec[i]:
            vocGroupRec[i - 1] = vocGroupRec[i - 1].replace("|ū", "").replace("|ā", "").replace("|ī", "").replace("|ō", "")


    if not "|[" in vocGroupRec[1] and not vocGroupRec[1] == "":
        vocGroupRec[1] = "|[" + vocGroupRec[1]
        vocGroupEdit[1] = "[" + vocGroupEdit[1]

    parsedLexicalItem = []

    if len(transcription) == 3 and transcription[1] == "":
        transcription[1] = "∅"
        consGroup[1] = "∅"
        consGroupIPA[1] = "∅"
        vocGroup[1] = "∅"
        vocGroupEdit[1] = "∅"
        vocGroupRec[1] = "∅"
        IDVowel[1] = "∅"

    parsedLexicalItem.append(transcription)
    parsedLexicalItem.append(consGroup)
    parsedLexicalItem.append(consGroupIPA)
    parsedLexicalItem.append(vocGroup)
    parsedLexicalItem.append(vocGroupEdit)
    parsedLexicalItem.append(vocGroupRec)
    parsedLexicalItem.append(IDVowel)

    parsedLexicalItem.insert(0, 2)
    return(parsedLexicalItem)