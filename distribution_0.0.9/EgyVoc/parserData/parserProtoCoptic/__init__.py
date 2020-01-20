def parseProtoCoptic (copticBase):

    CopticForm = copticBase["CopticForm"]
    Phonemes = copticBase["Phonemes"].split(".")
    PhonemeClasses = copticBase["PhonemeClasses"].split(".")
    Stress = copticBase["Stress"].split(".")
    VowelLength = copticBase["VowelLength"].split(".")

    if PhonemeClasses[0] == "V":
        Phonemes.insert(0, "ʔ")
        PhonemeClasses.insert(0, "C")
        Stress.insert(0, "0")
        VowelLength.insert(0, "0")

    if PhonemeClasses[-1] == "V":
        Phonemes.append("ʔ")
        PhonemeClasses.append("C")
        Stress.append("0")
        VowelLength.append("0")

    if VowelLength[-3] == "S" and PhonemeClasses[-2] == "C" and PhonemeClasses[-1] == "C":
        Phonemes.append("ə")
        PhonemeClasses.append("V")
        Stress.append("U")
        VowelLength.append("u")

    for i in range(0, len(VowelLength)-2):
        if VowelLength[i] == "L" and PhonemeClasses[i + 1] == "C" and PhonemeClasses[i + 2] == "C":
            Phonemes.insert(i+2, "ə")
            PhonemeClasses.insert(i+2, "V")
            Stress.insert(i+2, "U")
            VowelLength.insert(i+2, "u")

    if len(Phonemes) > 2 and PhonemeClasses[0] == "C" and PhonemeClasses[1] == "C" and PhonemeClasses[2] == "V":
        Phonemes.insert(1, "ə")
        PhonemeClasses.insert(1, "V")
        Stress.insert(1, "U")
        VowelLength.insert(1, "u")

    if len(Phonemes) > 3 and PhonemeClasses[0] == "C" and PhonemeClasses[1] == "C" and PhonemeClasses[2] == "C" and PhonemeClasses[3] == "V":
        Phonemes.insert(1, "ə")
        PhonemeClasses.insert(1, "V")
        Stress.insert(1, "U")
        VowelLength.insert(1, "u")

    if PhonemeClasses[-1] == "C" and PhonemeClasses[-2] == "C" and PhonemeClasses[-3] == "V":
        if VowelLength[-3] == "L":
            Phonemes.insert(-1, "ə")
            PhonemeClasses.insert(-1, "V")
            Stress.insert(-1, "U")
            VowelLength.insert(-1, "u")

        elif VowelLength[-3] == "S":
            Phonemes.append("ə")
            PhonemeClasses.append("V")
            Stress.append("U")
            VowelLength.append("u")

    if PhonemeClasses[-1] == "C" and PhonemeClasses[-2] == "V":
        if VowelLength[-2] == "L":
            Phonemes.append("ə")
            PhonemeClasses.append("V")
            Stress.append("U")
            VowelLength.append("u")


    if "|" in copticBase["Phonemes"]:
        print ("irregularity")
    else:
        PhonemesTemp = ".".join(Phonemes)
        PhonemesTemp = PhonemesTemp.replace("ō", "ā")
        PhonemesTemp = PhonemesTemp.replace("ē", "ī|ū")
        PhonemesTemp = PhonemesTemp.replace("e", "i|u")
        PhonemesTemp = PhonemesTemp.replace("a", "i|u")
        PhonemesTemp = PhonemesTemp.replace("o", "a")


        PhonemesTemp = PhonemesTemp.replace("ī.r", "ū.r")

        PhonemesTemp = PhonemesTemp.replace("i|u.h", "i|u|a.h")
        PhonemesTemp = PhonemesTemp.replace("i|u.ʔ", "i|u|a.ʔ")


    results = {}

    results["CopticForm"] = CopticForm
    results["Phonemes"] = PhonemesTemp
    results["PhonemeClasses"] = ".".join(PhonemeClasses)
    results["Stress"] = ".".join(Stress)
    results["VowelLength"] = ".".join(VowelLength)

    return results