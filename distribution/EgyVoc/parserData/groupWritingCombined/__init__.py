from ..dependencies.interfaceFAAL import interfaceFAAL
from ..groupWritingPeriod1 import parseGroupWriting_1
from ..groupWritingPeriod2 import parseGroupWriting_2
from ..groupWritingPeriod3 import parseGroupWriting_3
from ..groupWritingPeriod4 import parseGroupWriting_4
import itertools

import json

from ..dependencies.multiMatch import multiMatch

def parseGroupWritingForms(formsToParse):


    period1 = formsToParse["Period_1"]
    period2 = formsToParse["Period_2"]
    period3 = formsToParse["Period_3"]
    period4 = formsToParse["Period_4"]

    #correct dU in tU
    period1 = period1.replace("dU", "tU")
    period2 = period2.replace("dU", "tU")
    period3 = period3.replace("dU", "tU")
    period4 = period4.replace("dU", "tU")

    period11Parsed = parseGroupWriting_1(period1)
    period12Parsed = parseGroupWriting_2(period2)
    period13Parsed = parseGroupWriting_3(period3)
    period14Parsed = parseGroupWriting_4(period4)

    counterPeriods = 0

    if not period1 == "":
        counterPeriods = counterPeriods + 1
    if not period2 == "":
        counterPeriods = counterPeriods + 1
    if not period3 == "":
        counterPeriods = counterPeriods + 1
    if not period4 == "":
        counterPeriods = counterPeriods + 1


    if counterPeriods > 1:
        #print (period13Parsed)

        formsPeriods = []

        if not period11Parsed[1][1] == "∅":
            formsPeriods.append(period11Parsed)

        if not period12Parsed[1][1] == "∅":
            formsPeriods.append(period12Parsed)

        if not period13Parsed[1][1] == "∅":
            formsPeriods.append(period13Parsed)

        if not period14Parsed[1][1] == "∅":
            formsPeriods.append(period14Parsed)


        compare = []

        for a, b in itertools.combinations(formsPeriods, 2):
            entry = []
            entry.append(a)
            entry.append(b)
            compare.append(entry)

        matches = []

        for pair in compare:
            match = {"ID_A" : pair[0][0], "Form_A" : "".join(pair[0][3]).replace("#", "").replace("$", ""), "ID_B" : pair[1][0], "Form_B" : "".join(pair[1][3]).replace("#", "").replace("$", "")}
            match["Form_A"] = match["Form_A"].replace("š", "ʃ")\
                .replace("ꜣ", "ʔ")\
                .replace("ꜥ", "ʕ")\
                .replace("ṯ", "c")\
                .replace("ḏ", "ɟ")\
                .replace("ẖ", "ç")\
                .replace("ḫ", "χ")\
                .replace("ḥ", "ħ")\
                .replace("y", "ɥ")
            match["Form_B"] = match["Form_A"].replace("š", "ʃ") \
                .replace("ꜣ", "ʔ") \
                .replace("ꜥ", "ʕ") \
                .replace("ṯ", "c") \
                .replace("ḏ", "ɟ") \
                .replace("ẖ", "ç") \
                .replace("ḫ", "χ") \
                .replace("ḥ", "ħ") \
                .replace("y", "ɥ")
            resultComparison = interfaceFAAL(match["Form_A"], match["Form_B"])
            match["GlobScore"] = resultComparison["bestAlignGlobal"]
            match["AlignmentWordA"] = (resultComparison["wordWithDiacritics_1"]+"£").replace("┊", "").replace("￤", "").replace(":", "").replace("  £", "")
            match["AlignmentWordA"] = match["AlignmentWordA"].replace("ʃ", "š") \
                .replace("ʔ", "ꜣ") \
                .replace("ʕ", "ꜥ") \
                .replace("c", "ṯ") \
                .replace("ɟ", "ḏ") \
                .replace("ç", "ẖ") \
                .replace("χ", "ḫ") \
                .replace("ħ", "ḥ") \
                .replace("ɥ", "y")
            match["AlignmentWordB"] = (resultComparison["wordWithDiacritics_2"]+"£").replace("┊", "").replace("￤", "").replace(":", "").replace("  £", "")
            matches.append(match)

            match["AlignmentWordB"] = match["AlignmentWordB"].replace("ʃ", "š") \
                .replace("ʔ", "ꜣ") \
                .replace("ʕ", "ꜥ") \
                .replace("c", "ṯ") \
                .replace("ɟ", "ḏ") \
                .replace("ç", "ẖ") \
                .replace("χ", "ḫ") \
                .replace("ħ", "ḥ") \
                .replace("ɥ", "y")



        alignments = multiMatch(matches)

        #print ("===")



        #for item in alignments:
        #    print (item)

        alignmnet_1 = False
        alignmnet_2 = False
        alignmnet_3 = False
        alignmnet_4 = False

        nr_Letters = 0

        for alignment in alignments:
            if alignment[0] == 1:
                alignmnet_1 = True
                period11ParsedEdited = period11Parsed.copy()
                idx_Lett = 1
                for letter in alignment[1]:
                    if not letter == period11ParsedEdited[3][idx_Lett]:
                        period11ParsedEdited[1].insert(idx_Lett, "∅")
                        period11ParsedEdited[2].insert(idx_Lett, "∅")
                        period11ParsedEdited[3].insert(idx_Lett, "∅")
                        period11ParsedEdited[4].insert(idx_Lett, "∅")
                        period11ParsedEdited[5].insert(idx_Lett, "∅")
                        period11ParsedEdited[6].insert(idx_Lett, "∅")
                        period11ParsedEdited[7].insert(idx_Lett, "∅")
                        #idx_Lett = idx_Lett + 1
                    idx_Lett = idx_Lett + 1
                nr_Letters = idx_Lett-1

            if alignment[0] == 2:
                alignmnet_2 = True
                period12ParsedEdited = period12Parsed.copy()
                idx_Lett = 1
                for letter in alignment[1]:
                    if not letter == period12ParsedEdited[3][idx_Lett]:
                        period12ParsedEdited[1].insert(idx_Lett, "∅")
                        period12ParsedEdited[2].insert(idx_Lett, "∅")
                        period12ParsedEdited[3].insert(idx_Lett, "∅")
                        period12ParsedEdited[4].insert(idx_Lett, "∅")
                        period12ParsedEdited[5].insert(idx_Lett, "∅")
                        period12ParsedEdited[6].insert(idx_Lett, "∅")
                        period12ParsedEdited[7].insert(idx_Lett, "∅")
                        #idx_Lett = idx_Lett + 1
                    idx_Lett = idx_Lett + 1
                nr_Letters = idx_Lett - 1

            if alignment[0] == 3:
                alignmnet_3 = True
                period13ParsedEdited = period13Parsed.copy()
                idx_Lett = 1
                for letter in alignment[1]:
                    if not letter == period13ParsedEdited[3][idx_Lett]:
                        period13ParsedEdited[1].insert(idx_Lett, "∅")
                        period13ParsedEdited[2].insert(idx_Lett, "∅")
                        period13ParsedEdited[3].insert(idx_Lett, "∅")
                        period13ParsedEdited[4].insert(idx_Lett, "∅")
                        period13ParsedEdited[5].insert(idx_Lett, "∅")
                        period13ParsedEdited[6].insert(idx_Lett, "∅")
                        period13ParsedEdited[7].insert(idx_Lett, "∅")
                        # idx_Lett = idx_Lett + 1
                    idx_Lett = idx_Lett + 1
                nr_Letters = idx_Lett - 1

            if alignment[0] == 4:
                alignmnet_4 = True
                period14ParsedEdited = period14Parsed.copy()
                idx_Lett = 1
                for letter in alignment[1]:
                    if not letter == period14ParsedEdited[3][idx_Lett]:
                        period14ParsedEdited[1].insert(idx_Lett, "∅")
                        period14ParsedEdited[2].insert(idx_Lett, "∅")
                        period14ParsedEdited[3].insert(idx_Lett, "∅")
                        period14ParsedEdited[4].insert(idx_Lett, "∅")
                        period14ParsedEdited[5].insert(idx_Lett, "∅")
                        period14ParsedEdited[6].insert(idx_Lett, "∅")
                        period14ParsedEdited[7].insert(idx_Lett, "∅")
                        # idx_Lett = idx_Lett + 1
                    idx_Lett = idx_Lett + 1
                nr_Letters = idx_Lett - 1

        if alignmnet_1 == False:
            period11ParsedEdited = period11Parsed.copy()
            for i in range (0, nr_Letters-1 ):
                period11ParsedEdited[1].insert(i+1, "∅")
                period11ParsedEdited[2].insert(i+1, "∅")
                period11ParsedEdited[3].insert(i+1, "∅")
                period11ParsedEdited[4].insert(i+1, "∅")
                period11ParsedEdited[5].insert(i+1, "∅")
                period11ParsedEdited[6].insert(i+1, "∅")
                period11ParsedEdited[7].insert(i+1, "∅")

        if alignmnet_2 == False:
            period12ParsedEdited = period12Parsed.copy()
            for i in range (0, nr_Letters-1 ):
                period12ParsedEdited[1].insert(i+1, "∅")
                period12ParsedEdited[2].insert(i+1, "∅")
                period12ParsedEdited[3].insert(i+1, "∅")
                period12ParsedEdited[4].insert(i+1, "∅")
                period12ParsedEdited[5].insert(i+1, "∅")
                period12ParsedEdited[6].insert(i+1, "∅")
                period12ParsedEdited[7].insert(i+1, "∅")

        if alignmnet_3 == False:
            period13ParsedEdited = period13Parsed.copy()
            for i in range (0, nr_Letters-1 ):
                period13ParsedEdited[1].insert(i+1, "∅")
                period13ParsedEdited[2].insert(i+1, "∅")
                period13ParsedEdited[3].insert(i+1, "∅")
                period13ParsedEdited[4].insert(i+1, "∅")
                period13ParsedEdited[5].insert(i+1, "∅")
                period13ParsedEdited[6].insert(i+1, "∅")
                period13ParsedEdited[7].insert(i+1, "∅")

        if alignmnet_4 == False:
            period14ParsedEdited = period14Parsed.copy()
            for i in range (0, nr_Letters-1 ):
                period14ParsedEdited[1].insert(i+1, "∅")
                period14ParsedEdited[2].insert(i+1, "∅")
                period14ParsedEdited[3].insert(i+1, "∅")
                period14ParsedEdited[4].insert(i+1, "∅")
                period14ParsedEdited[5].insert(i+1, "∅")
                period14ParsedEdited[6].insert(i+1, "∅")
                period14ParsedEdited[7].insert(i+1, "∅")


        #for item in period11ParsedEdited:
        #   print (item)
        #for item in period12ParsedEdited:
        #   print (item)
        #for item in period13ParsedEdited:
        #   print (item)
        #for item in period14ParsedEdited:
        #   print (item)

        #print ()

        #reorganize
        alignedForms = {}



        alignedForms[period11ParsedEdited[0]] = {}
        alignedForms[period11ParsedEdited[0]]["ID"] = period11ParsedEdited[0]
        alignedForms[period11ParsedEdited[0]]["Irregularities"] = "False"
        alignedForms[period11ParsedEdited[0]]["Form"] = period11ParsedEdited[1]
        alignedForms[period11ParsedEdited[0]]["Consonants"] = period11ParsedEdited[2]
        alignedForms[period11ParsedEdited[0]]["IPA_Cons"] = period11ParsedEdited[3]
        for i in range(0, len(alignedForms[period11ParsedEdited[0]]["IPA_Cons"])):
            alignedForms[period11ParsedEdited[0]]["IPA_Cons"][i] = alignedForms[period11ParsedEdited[0]]["IPA_Cons"][i].replace("š", "ʃ")\
                .replace("ꜣ", "ʔ")\
                .replace("ꜥ", "ʕ")\
                .replace("ṯ", "c")\
                .replace("ḏ", "ɟ")\
                .replace("ẖ", "ç")\
                .replace("ḫ", "χ")\
                .replace("ḥ", "ħ")\
                .replace("y", "ɥ")


        alignedForms[period11ParsedEdited[0]]["VocClass"] = period11ParsedEdited[4]
        alignedForms[period11ParsedEdited[0]]["VocClassEdit"] = period11ParsedEdited[5]
        alignedForms[period11ParsedEdited[0]]["VocRec"] = period11ParsedEdited[6]
        alignedForms[period11ParsedEdited[0]]["VocCat"] = period11ParsedEdited[7]

        alignedForms[period12ParsedEdited[0]] = {}
        alignedForms[period12ParsedEdited[0]]["ID"] = period12ParsedEdited[0]
        alignedForms[period12ParsedEdited[0]]["Irregularities"] = "False"
        alignedForms[period12ParsedEdited[0]]["Form"] = period12ParsedEdited[1]
        alignedForms[period12ParsedEdited[0]]["Consonants"] = period12ParsedEdited[2]
        alignedForms[period12ParsedEdited[0]]["IPA_Cons"] = period12ParsedEdited[3]
        for i in range(0, len(alignedForms[period12ParsedEdited[0]]["IPA_Cons"])):
            alignedForms[period12ParsedEdited[0]]["IPA_Cons"][i] = alignedForms[period12ParsedEdited[0]]["IPA_Cons"][i].replace("š", "ʃ")\
                .replace("ꜣ", "ʔ")\
                .replace("ꜥ", "ʕ")\
                .replace("ṯ", "c")\
                .replace("ḏ", "ɟ")\
                .replace("ẖ", "ç")\
                .replace("ḫ", "χ")\
                .replace("ḥ", "ħ")\
                .replace("y", "ɥ")

        alignedForms[period12ParsedEdited[0]]["VocClass"] = period12ParsedEdited[4]
        alignedForms[period12ParsedEdited[0]]["VocClassEdit"] = period12ParsedEdited[5]
        alignedForms[period12ParsedEdited[0]]["VocRec"] = period12ParsedEdited[6]
        alignedForms[period12ParsedEdited[0]]["VocCat"] = period12ParsedEdited[7]

        alignedForms[period13ParsedEdited[0]] = {}
        alignedForms[period13ParsedEdited[0]]["ID"] = period13ParsedEdited[0]
        alignedForms[period13ParsedEdited[0]]["Irregularities"] = "False"
        alignedForms[period13ParsedEdited[0]]["Form"] = period13ParsedEdited[1]
        alignedForms[period13ParsedEdited[0]]["Consonants"] = period13ParsedEdited[2]
        alignedForms[period13ParsedEdited[0]]["IPA_Cons"] = period13ParsedEdited[3]
        for i in range(0, len(alignedForms[period13ParsedEdited[0]]["IPA_Cons"])):
            alignedForms[period13ParsedEdited[0]]["IPA_Cons"][i] = alignedForms[period13ParsedEdited[0]]["IPA_Cons"][i].replace("š", "ʃ")\
                .replace("ꜣ", "ʔ")\
                .replace("ꜥ", "ʕ")\
                .replace("ṯ", "c")\
                .replace("ḏ", "ɟ")\
                .replace("ẖ", "ç")\
                .replace("ḫ", "χ")\
                .replace("ḥ", "ħ")\
                .replace("y", "ɥ")
        alignedForms[period13ParsedEdited[0]]["VocClass"] = period13ParsedEdited[4]
        alignedForms[period13ParsedEdited[0]]["VocClassEdit"] = period13ParsedEdited[5]
        alignedForms[period13ParsedEdited[0]]["VocRec"] = period13ParsedEdited[6]
        alignedForms[period13ParsedEdited[0]]["VocCat"] = period13ParsedEdited[7]

        alignedForms[period14ParsedEdited[0]] = {}
        alignedForms[period14ParsedEdited[0]]["ID"] = period14ParsedEdited[0]
        alignedForms[period14ParsedEdited[0]]["Irregularities"] = "False"
        alignedForms[period14ParsedEdited[0]]["Form"] = period14ParsedEdited[1]
        alignedForms[period14ParsedEdited[0]]["Consonants"] = period14ParsedEdited[2]
        alignedForms[period14ParsedEdited[0]]["IPA_Cons"] = period14ParsedEdited[3]
        for i in range(0, len(alignedForms[period14ParsedEdited[0]]["IPA_Cons"])):
            alignedForms[period14ParsedEdited[0]]["IPA_Cons"][i] = alignedForms[period14ParsedEdited[0]]["IPA_Cons"][i].replace("š", "ʃ")\
                .replace("ꜣ", "ʔ")\
                .replace("ꜥ", "ʕ")\
                .replace("ṯ", "c")\
                .replace("ḏ", "ɟ")\
                .replace("ẖ", "ç")\
                .replace("ḫ", "χ")\
                .replace("ḥ", "ħ")\
                .replace("y", "ɥ")
        alignedForms[period14ParsedEdited[0]]["VocClass"] = period14ParsedEdited[4]
        alignedForms[period14ParsedEdited[0]]["VocClassEdit"] = period14ParsedEdited[5]
        alignedForms[period14ParsedEdited[0]]["VocRec"] = period14ParsedEdited[6]
        alignedForms[period14ParsedEdited[0]]["VocCat"] = period14ParsedEdited[7]


        #Flag as "irregularity == True" if consonant is missing

        if "∅" in "".join(alignedForms[period11ParsedEdited[0]]["Form"]):
            alignedForms[period11ParsedEdited[0]]["Irregularities"] = "True"
        if "∅" in "".join(alignedForms[period12ParsedEdited[0]]["Form"]):
            alignedForms[period12ParsedEdited[0]]["Irregularities"] = "True"
        if "∅" in "".join(alignedForms[period13ParsedEdited[0]]["Form"]):
            alignedForms[period13ParsedEdited[0]]["Irregularities"] = "True"
        if "∅" in "".join(alignedForms[period14ParsedEdited[0]]["Form"]):
            alignedForms[period14ParsedEdited[0]]["Irregularities"] = "True"

        #print ("-----")
        #for key in alignedForms:
        #    if alignedForms[key]["Irregularities"] == "True":
        #        print (alignedForms[key])

        #print ("-----")

        #print ("-----")
        #for key in alignedForms:
        #    if alignedForms[key]["Irregularities"] == "False":
        #        print (alignedForms[key])

        #print ("-----")

        #Create dataset
        consonantsDataset = []
        vowelsDatasetRec = []
        vowelsDatasetClass = []

        for key in alignedForms:
            if alignedForms[key]["Irregularities"] == "False":
                consonantsDataset.append([alignedForms[key]["ID"], alignedForms[key]["IPA_Cons"]])
                vowelsDatasetRec.append([alignedForms[key]["ID"], alignedForms[key]["VocRec"], alignedForms[key]["VocCat"]])
                vowelsDatasetClass.append([alignedForms[key]["ID"], alignedForms[key]["VocClassEdit"], alignedForms[key]["VocCat"]])

        vowelsDatasetRecPrePost = []
        vowelsDatasetClassPrePost = []



        #print (vowelsDatasetRec)

        #print ()

        for period in range(0,len(vowelsDatasetRec)):

            periodWord = vowelsDatasetRec[period][0]
            periodEntryRec = ([["#", "#"]])
            periodEntryClass = ([["#", "#"]])
            for i in range(1, len(vowelsDatasetRec[0][1])-1):
                periodEntryRec.append([vowelsDatasetRec[period][1][i], vowelsDatasetRec[period][1][i+1]])
                periodEntryClass.append([vowelsDatasetClass[period][1][i], vowelsDatasetClass[period][1][i+1]])


            vowelsDatasetRecPrePost.append([periodWord, periodEntryRec])
            vowelsDatasetClassPrePost.append([periodWord, periodEntryClass])

        #print (vowelsDatasetRecPrePost)
        #print (vowelsDatasetClassPrePost)
        #print ()

        #start analysis

        #period 3 and 4: final U = jw - if not jw -> cambiare gli algo precedenti jw = [U in the preceding

        for i in range(0,len(vowelsDatasetClassPrePost)):
            if vowelsDatasetClassPrePost[i][0] > 2 and not "[" in vowelsDatasetClassPrePost[i][1][-1][0]:
                vowelsDatasetClassPrePost[i][1][-1][0] = "$"
                vowelsDatasetClassPrePost[i][1][-2][1] = vowelsDatasetClassPrePost[i][1][-2][1] + "]"
                vowelsDatasetClassPrePost[i][1][-2][1] = vowelsDatasetClassPrePost[i][1][-2][1].replace("<U]", "<U")
                vowelsDatasetClassPrePost[i][1][-2][1] = vowelsDatasetClassPrePost[i][1][-2][1].replace("<Ɔ]", "<Ɔ")

        #if there is [U or U] -> generalize

        for i in range(0,len(vowelsDatasetClassPrePost)):
            for n in range(0,len(vowelsDatasetClassPrePost[0][1])):
                if vowelsDatasetClassPrePost[i][1][n][0] == "[U" or \
                        vowelsDatasetClassPrePost[i][1][n][1] == "U]":
                    vowelsDatasetClassPrePost[i][1][n][0] = vowelsDatasetClassPrePost[i][1][n][0].replace("A", "U")
                    vowelsDatasetClassPrePost[i][1][n][1] = vowelsDatasetClassPrePost[i][1][n][1].replace("A", "U")

        #extract likly vowels

        vowelsDatasetClassPrePostEdited = vowelsDatasetClassPrePost.copy()

        #print ("- - - - -")
        #print (vowelsDatasetClassPrePost)

        for i in range(0,len(vowelsDatasetClassPrePost)):

            for n in range(0,len(vowelsDatasetClassPrePostEdited[0][1])):
                if "U" in vowelsDatasetClassPrePostEdited[i][1][n][0] == 'U]':
                    vowelsDatasetClassPrePostEdited[i][1][n][0] = vowelsDatasetClassPrePostEdited[i][1][n][1].replace("]", "")
                if "U" in vowelsDatasetClassPrePostEdited[i][1][n][1] == '[U':
                    vowelsDatasetClassPrePostEdited[i][1][n][1] = vowelsDatasetClassPrePostEdited[i][1][n][0].replace("[", "")
                if vowelsDatasetClassPrePostEdited[i][1][n] == ["#","#"]:
                    vowelsDatasetClassPrePostEdited[i][1][n] = "#"
                elif vowelsDatasetClassPrePostEdited[i][1][n] == ["$","$"]:
                    vowelsDatasetClassPrePostEdited[i][1][n] = "$"
                elif vowelsDatasetClassPrePostEdited[i][1][n] == ['U>', '<U']:
                    vowelsDatasetClassPrePostEdited[i][1][n] = "⤫"
                elif vowelsDatasetClassPrePostEdited[i][1][n] == ['Ɔ>', '<Ɔ']:
                    vowelsDatasetClassPrePostEdited[i][1][n] = "⤫"
                elif vowelsDatasetClassPrePostEdited[i][1][n] == ['[U', 'U]']:
                    vowelsDatasetClassPrePostEdited[i][1][n] = "U"
                elif "U" in vowelsDatasetClassPrePostEdited[i][1][n][0] and \
                        "U" in vowelsDatasetClassPrePostEdited[i][1][n][1]:
                    vowelsDatasetClassPrePostEdited[i][1][n] = "U"
                    if len(vowelsDatasetClassPrePostEdited[i][1][n - 1]) > 1:
                        vowelsDatasetClassPrePostEdited[i][1][n - 1][1] = vowelsDatasetClassPrePostEdited[i][1][n - 1][0]
                    if "U" in vowelsDatasetClassPrePostEdited[i][1][n + 1][0]:
                        vowelsDatasetClassPrePostEdited[i][1][n + 1][0] = vowelsDatasetClassPrePostEdited[i][1][n + 1][1]
                elif "U" in vowelsDatasetClassPrePostEdited[i][1][n][0] and \
                        "Ɔ" in vowelsDatasetClassPrePostEdited[i][1][n][1]:
                    vowelsDatasetClassPrePostEdited[i][1][n] = "Ɔ"
                    if len(vowelsDatasetClassPrePostEdited[i][1][n - 1]) > 1:
                        vowelsDatasetClassPrePostEdited[i][1][n - 1][1] = vowelsDatasetClassPrePostEdited[i][1][n - 1][0]
                    if "Ɔ" in vowelsDatasetClassPrePostEdited[i][1][n + 1][0]:
                        vowelsDatasetClassPrePostEdited[i][1][n + 1][0] = vowelsDatasetClassPrePostEdited[i][1][n + 1][1]
                elif "Ɔ" in vowelsDatasetClassPrePostEdited[i][1][n][0] and \
                        "U" in vowelsDatasetClassPrePostEdited[i][1][n][1]:
                    vowelsDatasetClassPrePostEdited[i][1][n] = "Ɔ"
                    if vowelsDatasetClassPrePostEdited[i][1][n - 1] == "⤫":
                        vowelsDatasetClassPrePostEdited[i][1][n - 2][1] = vowelsDatasetClassPrePostEdited[i][1][n - 2][0]
                    else:
                        vowelsDatasetClassPrePostEdited[i][1][n - 1][1] = vowelsDatasetClassPrePostEdited[i][1][n - 1][0]
                    if "U" in vowelsDatasetClassPrePostEdited[i][1][n + 1][0]:
                        vowelsDatasetClassPrePostEdited[i][1][n + 1][0] = vowelsDatasetClassPrePostEdited[i][1][n + 1][1]
                elif "Ɔ" in vowelsDatasetClassPrePostEdited[i][1][n][0] and \
                        "Ɔ" in vowelsDatasetClassPrePostEdited[i][1][n][1]:
                    vowelsDatasetClassPrePostEdited[i][1][n] = "Ɔ"
                    if len(vowelsDatasetClassPrePostEdited[i][1][n - 1]) > 1:
                        vowelsDatasetClassPrePostEdited[i][1][n - 1][1] = vowelsDatasetClassPrePostEdited[i][1][n - 1][0]
                    vowelsDatasetClassPrePostEdited[i][1][n + 1][0] = vowelsDatasetClassPrePostEdited[i][1][n + 1][1]
                elif "A" in vowelsDatasetClassPrePostEdited[i][1][n][0] and \
                        "A" in vowelsDatasetClassPrePostEdited[i][1][n][1]:
                    vowelsDatasetClassPrePostEdited[i][1][n] = "A"
                elif "A" in vowelsDatasetClassPrePostEdited[i][1][n][0] and \
                        "$" in vowelsDatasetClassPrePostEdited[i][1][n][1]:
                    vowelsDatasetClassPrePostEdited[i][1][n] = "$"
                elif "⤫" in vowelsDatasetClassPrePostEdited[i][1][n][0]:
                    vowelsDatasetClassPrePostEdited[i][1][n] = "⤫"
                elif "⤫" in vowelsDatasetClassPrePostEdited[i][1][n][1]:
                    vowelsDatasetClassPrePostEdited[i][1][n][1] = vowelsDatasetClassPrePostEdited[i][1][n][0]

            for n in range(0, len(vowelsDatasetClassPrePostEdited[0][1])):
                if len(vowelsDatasetClassPrePostEdited[i][1][n]) > 1:
                    if "U" in vowelsDatasetClassPrePostEdited[i][1][n][0] and \
                        "U" in vowelsDatasetClassPrePostEdited[i][1][n][1]:
                        vowelsDatasetClassPrePostEdited[i][1][n] = "U"
                    elif "A" in vowelsDatasetClassPrePostEdited[i][1][n][0] and \
                        "A" in vowelsDatasetClassPrePostEdited[i][1][n][1]:
                        vowelsDatasetClassPrePostEdited[i][1][n] = "A"

            for n in range(0, len(vowelsDatasetClassPrePostEdited[0][1])):
                if len(vowelsDatasetClassPrePostEdited[i][1][n]) == 2:
                    vowelsDatasetClassPrePostEdited[i][1][n] = vowelsDatasetClassPrePostEdited[i][1][n][0] + "|" + vowelsDatasetClassPrePostEdited[i][1][n][1]

            if n > 0:
                if "|U" in vowelsDatasetClassPrePostEdited[i][1][n-1] and\
                    "U|" in vowelsDatasetClassPrePostEdited[i][1][n]:
                    vowelsDatasetClassPrePostEdited[i][1][n - 1] = vowelsDatasetClassPrePostEdited[i][1][n-1].replace("|U", "|U>")
                    vowelsDatasetClassPrePostEdited[i][1][n] = vowelsDatasetClassPrePostEdited[i][1][n].replace("U|", "<U|")

                if "⤫" in vowelsDatasetClassPrePostEdited[i][1][n-1] and\
                    "U|" in vowelsDatasetClassPrePostEdited[i][1][n]:
                    vowelsDatasetClassPrePostEdited[i][1][n] = "U"


            countU = 0
            for n in range(0, len(vowelsDatasetClassPrePostEdited[0][1])):
                if "U" in vowelsDatasetClassPrePostEdited[i][1][n]:
                    countU = countU + 1
            if countU == 1:
                for n in range(0, len(vowelsDatasetClassPrePostEdited[0][1])):
                    if "U" in vowelsDatasetClassPrePostEdited[i][1][n]:
                        vowelsDatasetClassPrePostEdited[i][1][n] = "U"





        #print (vowelsDatasetRecPrePost)

        #print ("====")
        #print (vowelsDatasetClassPrePostEdited)

        # se x in un periodo, x in tutti -> poi contare le U

        for i in range(0, len(vowelsDatasetClassPrePostEdited)):
            countU = 0
            for n in range(0, len(vowelsDatasetClassPrePostEdited[0][1])):
                if "⤫" in vowelsDatasetClassPrePostEdited[i][1][n]:
                    for z in range(0, len(vowelsDatasetClassPrePostEdited)):
                        vowelsDatasetClassPrePostEdited[z][1][n] = "⤫"
                if "U" in vowelsDatasetClassPrePostEdited[i][1][n]:
                    countU = countU + 1
                if n > 0:
                    if "⤫" in vowelsDatasetClassPrePostEdited[i][1][n - 1] and \
                            "U|" in vowelsDatasetClassPrePostEdited[i][1][n]:
                        vowelsDatasetClassPrePostEdited[i][1][n] = "U"
            if countU == 1:
                for n in range(0, len(vowelsDatasetClassPrePostEdited[0][1])):
                    if "U" in vowelsDatasetClassPrePostEdited[i][1][n]:
                        vowelsDatasetClassPrePostEdited[i][1][n] = "U"

        #change previous vowel, if word ends in -0 in any period:
        finalCons = False
        for i in range(0, len(vowelsDatasetClassPrePostEdited)):
            if vowelsDatasetClassPrePostEdited[i][1][-1] == "$":
                finalCons = True

        if finalCons == True:
            if "U" in vowelsDatasetClassPrePostEdited[i][1][-2]:
                for i in range(0, len(vowelsDatasetClassPrePostEdited)):
                    if "U" in vowelsDatasetClassPrePostEdited[i][1][-1]:
                        vowelsDatasetClassPrePostEdited[i][1][-2] = "U"
                    vowelsDatasetClassPrePostEdited[i][1][-1] = "$"




        #print (vowelsDatasetClassPrePostEdited)

        shortVowels = [["a1", "A", "A", "U", "U"]]
        shortVowels.append(["a1", "A", "A", "Ɔ", "Ɔ"])
        shortVowels.append(["a1", "A", "A", "Ɔ", "U"])
        shortVowels.append(["a1", "A", "A", "U", "Ɔ"])

        shortVowels.append(["a2", "Ɔ", "Ɔ", "Ɔ", "Ɔ"])
        #shortVowels.append(["a2", "U", "Ɔ", "Ɔ", "Ɔ"])
        #shortVowels.append(["a2", "Ɔ", "U", "Ɔ", "Ɔ"])
        shortVowels.append(["a2", "Ɔ", "Ɔ", "U", "Ɔ"])
        shortVowels.append(["a2", "Ɔ", "Ɔ", "Ɔ", "U"])
        #shortVowels.append(["a2", "U", "U", "Ɔ", "Ɔ"])
        #shortVowels.append(["a2", "U", "Ɔ", "U", "Ɔ"])
        #shortVowels.append(["a2", "U", "Ɔ", "Ɔ", "U"])
        #shortVowels.append(["a2", "Ɔ", "U", "U", "Ɔ"])
        #shortVowels.append(["a2", "Ɔ", "U", "Ɔ", "U"])
        shortVowels.append(["a2", "Ɔ", "Ɔ", "U", "U"])
        #shortVowels.append(["a2", "U", "U", "U", "Ɔ"])
        #shortVowels.append(["a2", "U", "U", "Ɔ", "U"])
        #shortVowels.append(["a2", "U", "Ɔ", "U", "U"])
        #shortVowels.append(["a2", "Ɔ", "U", "U", "U"])
        #shortVowels.append(["a2", "U", "U", "U", "U"])

        shortVowels.append(["a3", "A", "A", "A", "A"])
        shortVowels.append(["i", "A", "A", "A", "A"])
        shortVowels.append(["u", "Ɔ", "Ɔ", "A", "A"])
        shortVowels.append(["u", "U", "U", "A", "A"])
        shortVowels.append(["u", "Ɔ", "U", "A", "A"])
        shortVowels.append(["u", "U", "Ɔ", "A", "A"])
        #shortVowels.append(["u2", "Ɔ", "Ɔ", "A", "A"])

        unstressedVowels = [["ə", "A", "A", "A", "A"]]
        unstressedVowels.append(["ŭ", "U", "A", "A", "A"])
        unstressedVowels.append(["ŭ", "Ɔ", "A", "A", "A"])

        longVowels = [["ā1", "A", "U", "U", "U"]]
        longVowels.append(["ā1", "A", "Ɔ", "U", "U"])
        longVowels.append(["ā1", "A", "U", "Ɔ", "U"])
        longVowels.append(["ā1", "A", "U", "U", "Ɔ"])
        longVowels.append(["ā1", "A", "Ɔ", "Ɔ", "U"])
        longVowels.append(["ā1", "A", "Ɔ", "U", "Ɔ"])
        longVowels.append(["ā1", "A", "U", "Ɔ", "Ɔ"])
        longVowels.append(["ā1", "A", "Ɔ", "Ɔ", "Ɔ"])

        #longVowels.append(["ā2", "U", "U", "U", "U"])
        longVowels.append(["ā2", "Ɔ", "U", "U", "U"])
        #longVowels.append(["ā2", "U", "Ɔ", "U", "U"])
        #longVowels.append(["ā2", "U", "U", "Ɔ", "U"])
        #longVowels.append(["ā2", "U", "U", "U", "Ɔ"])
        longVowels.append(["ā2", "Ɔ", "Ɔ", "U", "U"])
        longVowels.append(["ā2", "Ɔ", "U", "Ɔ", "U"])
        longVowels.append(["ā2", "Ɔ", "U", "U", "Ɔ"])
        #longVowels.append(["ā2", "U", "Ɔ", "Ɔ", "U"])
        #longVowels.append(["ā2", "U", "Ɔ", "U", "Ɔ"])
        #longVowels.append(["ā2", "U", "U", "Ɔ", "Ɔ"])
        longVowels.append(["ā2", "Ɔ", "Ɔ", "Ɔ", "U"])
        longVowels.append(["ā2", "Ɔ", "Ɔ", "U", "Ɔ"])
        longVowels.append(["ā2", "Ɔ", "U", "Ɔ", "Ɔ"])
        #longVowels.append(["ā2", "U", "Ɔ", "Ɔ", "Ɔ"])
        longVowels.append(["ā2", "Ɔ", "Ɔ", "Ɔ", "Ɔ"])


        longVowels.append(["ī", "A", "A", "A", "A"])
        longVowels.append(["ū", "U", "U", "U", "A"])
        longVowels.append(["ū", "Ɔ", "U", "U", "A"])
        longVowels.append(["ū", "U", "Ɔ", "U", "A"])
        longVowels.append(["ū", "U", "U", "Ɔ", "A"])
        longVowels.append(["ū", "Ɔ", "Ɔ", "U", "A"])
        longVowels.append(["ū", "Ɔ", "U", "Ɔ", "A"])
        longVowels.append(["ū", "U", "Ɔ", "Ɔ", "A"])
        longVowels.append(["ū", "Ɔ", "Ɔ", "Ɔ", "A"])
        #longVowels.append(["ū2", "Ɔ", "Ɔ", "Ɔ", "A"])

        listVowels = []
        periodsVow = []
        for n in range(0, len(vowelsDatasetClassPrePostEdited)):
            periodsVow.append(vowelsDatasetClassPrePostEdited[n][0])
        listVowels.append(periodsVow)

        for i in range (0, len(vowelsDatasetClassPrePostEdited[0][1])):
            vowelSet = []
            for n in range(0, len(vowelsDatasetClassPrePostEdited)):
                vowelSet.append(vowelsDatasetClassPrePostEdited[n][1][i])
            listVowels.append(vowelSet)

        #print (listVowels)
        regular = True

        reconstructedVowels = []

        for i in range(1, len(listVowels)):
            long = True
            short = True
            vowelRec = ""
            #check it the next is a x
            if i < len(listVowels) -1:
                if "⤫" in listVowels[i+1][0]:
                    long = False
            if i < len(listVowels) -2:
                if "⤫" in listVowels[i+2][0]:
                    short = False
            if "#" in listVowels[i][0]:
                vowelRec = "#"
            if "$" in listVowels[i][0]:
                vowelRec = "$"
            if "⤫" in listVowels[i][0]:
                vowelRec = "⤫"
            if long == True:
                for vowel in longVowels:
                    isVowel = True
                    isO = False
                    for n in range(0, len(listVowels[i])):
                        if not vowel[listVowels[0][n]] in listVowels[i][n]:
                            isVowel = False
                            #remove false Ɔ in case forst period attestation is missing
                            if vowel[listVowels[0][n]] == "Ɔ":
                                isO = True
                    if not isVowel == False:
                        vowelRec = vowelRec + "|" + vowel[0]
                        if isO == False and not listVowels[0][0] == "1":
                            vowelRec = vowelRec.replace("|ā2","")
                    isO = False
            if short == True:
                for vowel in shortVowels:
                    isVowel = True
                    isO = False
                    for n in range(0, len(listVowels[i])):
                        if not vowel[listVowels[0][n]] in listVowels[i][n]:
                            isVowel = False
                            # remove false Ɔ in case forst period attestation is missing
                            if vowel[listVowels[0][n]] == "Ɔ":
                                isO = True
                    if not isVowel == False:
                        vowelRec = vowelRec + "|" + vowel[0]
                        if isO == False and not listVowels[0][0] == "1" and not listVowels[0][0] == "2":
                            vowelRec = vowelRec.replace("|a2","")
                    isO = False
            for vowel in unstressedVowels:
                isVowel = True
                for n in range(0, len(listVowels[i])):
                    if not vowel[listVowels[0][n]] in listVowels[i][n]:
                        isVowel = False
                if not isVowel == False:
                    vowelRec = vowelRec + "|" + vowel[0]
                    if not listVowels[0][0] == "1":
                        #replece the short |ŭ with |ə in case there is no attestation for period 1
                        vowelRec = vowelRec.replace("|ŭ", "|ə")
            if vowelRec == "":
                vowelRec = "irregularity"
                regular = False

            splitVowelRec = vowelRec.split("|")
            splitVowelRec = list(dict.fromkeys(splitVowelRec))

            newVowelRec = "|".join(splitVowelRec)

            #print ("----")
            reconstructedVowels.append(newVowelRec)

        earlierCons = consonantsDataset[0][1]

        for i in range(0, len(reconstructedVowels)):
            if not "|" in reconstructedVowels[i] and \
                    not "#" in reconstructedVowels[i] and \
                    not "$" in reconstructedVowels[i]:
                reconstructedVowels[i] = "|" + reconstructedVowels[i]


        #filter on the basis of consonats etc xxx
        for i in range (1, len(reconstructedVowels)-1):
            if not "ʕ" in earlierCons[i+1] and \
                    not "h" in earlierCons[i + 1] and \
                    not "ḥ" in earlierCons[i + 1] and \
                    not "ȟ" in earlierCons[i + 1] and \
                    not "ḫ" in earlierCons[i + 1] and \
                    not "ẖ" in earlierCons[i + 1] and \
                    not "x" in earlierCons[i + 1] and \
                    not "ç" in earlierCons[i + 1] and \
                    not "ħ" in earlierCons[i + 1]:
                reconstructedVowels[i] = reconstructedVowels[i].replace("|a3", "")
            if "ŭ" in reconstructedVowels[i]:
                reconstructedVowels[i] = "|ŭ"

        nrStressed = 0
        nrExclusiveStressed = 0
        for i in range (1, len(reconstructedVowels)):
            if "a" in reconstructedVowels[i] \
                or "i" in reconstructedVowels[i]\
                or "u" in reconstructedVowels[i]\
                or "ā" in reconstructedVowels[i]\
                or "ī" in reconstructedVowels[i]\
                or "ū" in reconstructedVowels[i]:
                nrStressed = nrStressed + 1
                if not "ə" in reconstructedVowels[i] and \
                        not "ŭ" in reconstructedVowels[i]:
                    nrExclusiveStressed = nrExclusiveStressed +1



        if nrStressed == 1:
            for i in range(1, len(reconstructedVowels)):
                if "a" in reconstructedVowels[i] \
                        or "i" in reconstructedVowels[i] \
                        or "u" in reconstructedVowels[i] \
                        or "ā" in reconstructedVowels[i] \
                        or "ī" in reconstructedVowels[i] \
                        or "ū" in reconstructedVowels[i]:
                    reconstructedVowels[i] = reconstructedVowels[i].replace("|ŭ", "").replace("|ə", "")

        # if only one stressed -> everything else unstressed

        if nrExclusiveStressed == 1:
            for i in range(1, len(reconstructedVowels)):
                if "ə" in reconstructedVowels[i] \
                    and "ŭ" in reconstructedVowels[i]:
                    reconstructedVowels[i] = "|ə|ŭ"
                elif "ə" in reconstructedVowels[i]:
                    reconstructedVowels[i] = "|ə"
                elif "ŭ" in reconstructedVowels[i]:
                    reconstructedVowels[i] = "|ŭ"

        if ("$" in reconstructedVowels[-1]):
            reconstructedVowels[-1] = "|ə|⤫"

        #remove 1 for the a:

        for i in range(1, len(reconstructedVowels)):
            reconstructedVowels[i] = reconstructedVowels[i].replace("1", "")

        #if stressed short -> next add |⤫

        for i in range(1, len(reconstructedVowels)-1):
            if ("a" in reconstructedVowels[i] \
                    or "i" in reconstructedVowels[i] \
                    or "u" in reconstructedVowels[i]) and\
                    not "⤫" in reconstructedVowels[i+1]:
                reconstructedVowels[i + 1] = "|⤫" + reconstructedVowels[i+1]
            elif ("a" in reconstructedVowels[i] \
                    or "i" in reconstructedVowels[i] \
                    or "u" in reconstructedVowels[i]) and\
                    "|⤫|ə" == reconstructedVowels[i+1] or\
                    "|ə|⤫" == reconstructedVowels[i+1]:
                reconstructedVowels[i + 1] = "|⤫"
            elif ("ā" in reconstructedVowels[i] \
                    or "ī" in reconstructedVowels[i] \
                    or "ū" in reconstructedVowels[i]) and\
                    "|⤫|ə" == reconstructedVowels[i+1] or\
                    "|ə|⤫" == reconstructedVowels[i+1]:
                reconstructedVowels[i + 1] = "|ə"




        reconstructedForm = []
        if regular == True:
            for i in range (0, len(earlierCons)-1):
                reconstructedForm.append(earlierCons[i])
                reconstructedForm.append(reconstructedVowels[i])
            for i in range (1, len(reconstructedForm)):
                if reconstructedForm[i] == "#" and reconstructedForm[i-1] == "#":
                    reconstructedForm.pop(i)
                    break
            for i in range(1, len(reconstructedForm)):
                if reconstructedForm[i] == "$" and reconstructedForm[i-1] == "$":
                    reconstructedForm.pop(i)
                    break
        reconstructedForm.append("$")

        #print ("=======")
        #print (reconstructedForm)
        #print (earlierCons)
        #print (reconstructedVowels)
        #print (regular)

        phonemeClass = "£"
        vowelLength = "£"
        vowelStress = "£"

        for letter in reconstructedForm:
            if not "#" in letter and not "$" in letter and not letter == "|⤫":
                if "|" in letter:
                    if "⤫" in letter:
                        phonemeClass = phonemeClass + ".v"
                    else:
                        phonemeClass = phonemeClass + ".V"
                    tempClass = ""
                    if ("ā" in letter or "ī" in letter or "ū" in letter):
                        tempClass = tempClass + "L"
                    if ("a" in letter or "i" in letter or "u" in letter):
                        tempClass = tempClass + "S"
                    if ("ə" in letter or "ŭ" in letter):
                        tempClass = tempClass + "u"

                    if tempClass == "L":
                        vowelLength = vowelLength + ".L"
                        vowelStress = vowelStress + ".S"
                    elif tempClass == "S":
                        vowelLength = vowelLength + ".S"
                        vowelStress = vowelStress + ".S"
                    elif tempClass == "u":
                        vowelLength = vowelLength + ".u"
                        vowelStress = vowelStress + ".U"
                    else:
                        vowelLength = vowelLength + ".l"
                        if not "u" in tempClass:
                            vowelStress = vowelStress + ".S"
                        else:
                            vowelStress = vowelStress + ".u"
                else:
                    phonemeClass = phonemeClass + ".C"
                    vowelLength = vowelLength + ".0"
                    vowelStress = vowelStress + ".0"

        phonemeClass = phonemeClass.replace("£.", "")
        vowelLength = vowelLength.replace("£.", "")
        vowelStress = vowelStress.replace("£.", "")



        phonemes = "£"


        for letter in reconstructedForm:
            letterTemp = "£" + letter
            letterTemp = letterTemp.replace("£|", "")
            letterTemp = letterTemp.replace("£", "")
            if not "#" in letterTemp and not "$" in letterTemp and not letterTemp == "⤫":
                phonemes = phonemes + "." + letterTemp

        phonemes = phonemes.replace("£.", "")


        results = {}

        results["Regular"] = regular
        results["Earlier_Cons"] = earlierCons
        results["Reconstr_Vow"] = reconstructedVowels
        results["Aligned_Forms"] = alignedForms
        results["Reconstructed_Form"] = reconstructedForm
        results["Phonemes"] = phonemes.replace("ʃ", "š") \
                .replace("ʔ", "ꜣ") \
                .replace("ʕ", "ꜥ") \
                .replace("c", "ṯ") \
                .replace("ɟ", "ḏ") \
                .replace("ç", "ẖ") \
                .replace("χ", "ḫ") \
                .replace("ħ", "ḥ") \
                .replace("ɥ", "y")
        results["PhonemesIPA"] = phonemes
        results["PhonemeClasses"] = phonemeClass
        results["Stress"] = vowelStress
        results["VowelLength"] = vowelLength

        earliestForm = ""
        periodEarliestForm = ""

        for item in results["Aligned_Forms"]:
            if not results["Aligned_Forms"][item]["Form"][1] == "∅":
                earliestForm = ".".join(results["Aligned_Forms"][item]["Form"]).replace("#.", "").replace(".$", "")
                periodEarliestForm = item
                break

        results["Earliest_Form"] = earliestForm
        results["PeriodEarliestForm"] = periodEarliestForm

        json_results = json.dumps(results, sort_keys=True, indent=3, ensure_ascii=False)
        #print(json_results)

        return results

    else:

        print ("Warning! Only one Group Writing spelling, not enough to reconstruct the vocalization.")
        print ()

        results = {}

        results["Regular"] = "Warning! Only one Group Writing spelling, not enough to reconstruct the vocalization."
        results["Earlier_Cons"] = "None"
        results["Reconstr_Vow"] = "None"
        results["Aligned_Forms"] = "None"
        results["Reconstructed_Form"] = "None"
        results["Phonemes"] = "None"
        results["PhonemesIPA"] = "None"
        results["PhonemeClasses"] = "None"
        results["Stress"] = "None"
        results["VowelLength"] = "None"

        return results