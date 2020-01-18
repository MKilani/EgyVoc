def multiMatch (matches):
    '''
    :param matches: format: <class 'list'>: [{'ID_A': int, 'Form_A': string, 'ID_B': int, 'Form_B': string, 'GlobScore': float, 'AlignmentWordA': string, 'AlignmentWordB': string}]
    :return: list of list
    '''

    matchesSorted = sorted(matches, key=lambda match: match["GlobScore"], reverse=True)

    #print(matchesSorted)

    alignments = []
    alignment = [matchesSorted[0]["ID_A"], matchesSorted[0]["AlignmentWordA"].split("  ")]
    alignments.append(alignment)
    alignment = [matchesSorted[0]["ID_B"], matchesSorted[0]["AlignmentWordB"].split("  ")]
    alignments.append(alignment)


    for match in matchesSorted:
        match_A = False
        match_B = False
        ID_match_A = 0
        ID_match_B = 0
        ID_alignment = 0
        for alignment in alignments:
            if alignment[0] == match["ID_A"]:
                match_A = True
                ID_match_A = ID_alignment
            if alignment[0] == match["ID_B"]:
                match_B = True
                ID_match_B = ID_alignment
            ID_alignment = ID_alignment + 1

        if (match_A == True and match_B == False) or (match_A == False and match_B == True):

            if match_A == True:
                newMatch_A = match["AlignmentWordA"].split("  ")
                newMatch_B = match["AlignmentWordB"].split("  ")
                for i in range(0, len(newMatch_A)):
                    if len(alignments[ID_match_A][1]) == i or len(newMatch_A) == i:
                        if len(newMatch_A) == i:
                            newMatch_A.append("0")
                            newMatch_B.append("0")
                        if len(alignments[ID_match_A][1]) == i:
                            for n in range(0, len(alignments)):
                                alignments[n][1].append("0")
                    else:
                        if not alignments[ID_match_A][1][i] == newMatch_A[i]:
                            if alignments[ID_match_A][1][i] == "0":
                                newMatch_A.insert(i, "0")
                                newMatch_B.insert(i, "0")
                            if newMatch_A[i] == "0":
                                for n in range(0, len(alignments)):
                                    alignments[n][1].insert(i, "0")

                for i in range(0, len(alignments[ID_match_A][1])):
                    if len(alignments[ID_match_A][1]) == i or len(newMatch_A) == i:
                        if len(newMatch_A) == i:
                            newMatch_A.append("0")
                            newMatch_B.append("0")
                        if len(alignments[ID_match_A][1]) == i:
                            for n in range(0, len(alignments)):
                                alignments[n][1].append("0")

                    else:
                        if not alignments[ID_match_A][1][i] == newMatch_A[i]:
                            if alignments[ID_match_A][1][i] == "0":
                                newMatch_A.insert(i, "0")
                                newMatch_B.insert(i, "0")
                            if newMatch_A[i] == "0":
                                for n in range(0, len(alignments)):
                                    alignments[n][1].insert(i, "0")
                new_entry = []
                new_entry.append(match["ID_B"])
                new_entry.append(newMatch_B)
                alignments.append(new_entry)

            if match_B == True:
                newMatch_B = match["AlignmentWordB"].split("  ")
                newMatch_A = match["AlignmentWordA"].split("  ")
                for i in range(0, len(newMatch_B)):
                    if len(alignments[ID_match_B][1]) == i or len(newMatch_B) == i:
                        if len(newMatch_B) == i:
                            newMatch_B.append("0")
                            newMatch_A.append("0")
                        if len(alignments[ID_match_B][1]) == i:
                            for n in range(0, len(alignments)):
                                alignments[n][1].append("0")
                    else:
                        if not alignments[ID_match_B][1][i] == newMatch_B[i]:
                            if alignments[ID_match_B][1][i] == "0":
                                newMatch_B.insert(i, "0")
                                newMatch_A.insert(i, "0")
                            if newMatch_B[i] == "0":
                                for n in range(0, len(alignments)):
                                    alignments[n][1].insert(i, "0")

                for i in range(0, len(alignments[ID_match_B])):
                    if len(alignments[ID_match_B][1]) == i or len(newMatch_B) == i:
                        if len(newMatch_B) == i:
                            newMatch_B.append("0")
                            newMatch_A.append("0")
                        if len(alignments[ID_match_B][1]) == i:
                            for n in range(0, len(alignments)):
                                alignments[n][1].append("0")
                    else:
                        if not alignments[ID_match_B][1][i] == newMatch_B[i]:
                            if alignments[ID_match_B][1][i] == "0":
                                newMatch_B.insert(i, "0")
                                newMatch_A.insert(i, "0")
                            if newMatch_B[i] == "0":
                                for n in range(0, len(alignments)):
                                    alignments[n][1].insert(i, "0")
                new_entry = []
                new_entry.append(match["ID_A"])
                new_entry.append(newMatch_A)
                alignments.append(new_entry)


    return alignments

