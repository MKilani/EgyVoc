from .parserData.copticSahidic_1_0 import parseCopticSahidic
from .parserData.groupWritingCombined import parseGroupWritingForms
from .parserData.parserProtoCoptic import parseProtoCoptic
from .parserData.joinReconstructions import joinReconstructions
from .parserData.joinReconstructions import joinCopticRoot
import os
import subprocess

def initializeFAAL():

    

    jarFolder = os.path.join(os.path.dirname(__file__), 'parserData', 'dependencies', 'FAAL_jar')

    process = subprocess.Popen('java -jar FAAL_jar_Global.jar',
                               cwd=jarFolder,
                               stdout=subprocess.PIPE, shell=True)

    while True:
        output = process.stdout.readline()
        if not output == '':
            print("FAAL jar is running...")
            break
    return process

def terminateFAAL(process):
    process.terminate()


def EgyVoc(SahidicWord = "", EgyptianRoot = "", GW_Period_1 = "", GW_Period_2 = "", GW_Period_3 = "", GW_Period_4 = "", verbose = True):




    GroupWritingForms = {}

    if not GW_Period_1 == "" or not GW_Period_2 == "" or not GW_Period_3 == "" or not GW_Period_4 == "":
        GroupWritingForms["Period_1"] = GW_Period_1
        GroupWritingForms["Period_2"] = GW_Period_2
        GroupWritingForms["Period_3"] = GW_Period_3
        GroupWritingForms["Period_4"] = GW_Period_4

    results = {}

    if not SahidicWord == "":
        if verbose == True:
            print ("* Transcription of the Coptic Form:")
            print()
        parsedSahidicWord = parseCopticSahidic(SahidicWord, verbose)
        protoSahidicCopticParsed = parseProtoCoptic(parsedSahidicWord)
        results["ProtoCoptic"] = protoSahidicCopticParsed

        if not EgyptianRoot == "":
            results["ProtoCoptic"] = joinCopticRoot(EgyptianRoot, protoSahidicCopticParsed)
        else:
            results["ProtoCoptic"]["EgyptianRoot"] = "None"
            results["ProtoCoptic"]["PhonemesIPA"] = results["ProtoCoptic"]["Phonemes"]



        if verbose == True:
            print ()
            print ("----")
            print()
            print("* ProtoCoptic Vocalization:")
            print()
            print ("CopticForm: " + results["ProtoCoptic"]["CopticForm"])
            print ("EgyptianRoot: " + results["ProtoCoptic"]["EgyptianRoot"])
            print ()
            print ("Reconstruction - PhonemesIPA: " + results["ProtoCoptic"]["PhonemesIPA"])
            print ("Reconstruction - Phonemes: " + results["ProtoCoptic"]["Phonemes"])
            print ("Reconstruction - Phoneme classes: " + results["ProtoCoptic"]["PhonemeClasses"])
            print ("Reconstruction - Stress: " + results["ProtoCoptic"]["Stress"])
            print ("Reconstruction - Vowel Length: " + results["ProtoCoptic"]["VowelLength"])
            print ()
            print ("----")
            print ()
    else:
        results["ProtoCoptic"] = None


    if not GroupWritingForms == {}:
        if verbose == True:
            print("* GroupWriting vocalization:")
            print ()
        resultsGroupWriting = parseGroupWritingForms(GroupWritingForms)
        results["GroupWriting_Voc"] = resultsGroupWriting
        if verbose == True and not results["GroupWriting_Voc"]["Earlier_Cons"] == "None":
            print("Regular: " + str(results["GroupWriting_Voc"]['Regular']))
            print("First attestation: " + results["GroupWriting_Voc"]['Earliest_Form'])
            print("First attestation: Period " + str(results["GroupWriting_Voc"]['PeriodEarliestForm']))
            print()
            print("Reconstruction - PhonemesIPA: " + results["GroupWriting_Voc"]['PhonemesIPA'])
            print("Reconstruction - Phonemes: " + results["GroupWriting_Voc"]['Phonemes'])
            print("Reconstruction - Phon. Classes: " + results["GroupWriting_Voc"]['PhonemeClasses'])
            print("Reconstruction - Stress: " + results["GroupWriting_Voc"]['Stress'])
            print("Reconstruction - Vowel Length: " + results["GroupWriting_Voc"]['VowelLength'])
            print ()
            print ("----")
            print ()
    else:
        results["GroupWriting_Voc"] = None

    if not SahidicWord == "" and not GroupWritingForms == {}:

        joinedVocalization = joinReconstructions(resultsGroupWriting, protoSahidicCopticParsed)
        results["Reconstructed_Voc_Matrix"] = joinedVocalization
        results["Reconstructed_VocalizationIPA"] = joinedVocalization["PhonemesIPA"].replace(".", "").replace("⤫", "")
        results["Reconstructed_Vocalization"] = joinedVocalization["Phonemes"].replace(".", "").replace("⤫", "")

        if verbose == True:
            print("* Joined reconstructed vocalization:")
            print ()
            print("Reconstructed vocalizationIPA: " + results["Reconstructed_VocalizationIPA"])
            print("Reconstructed vocalization: " + results["Reconstructed_Vocalization"])
            print()
            print("Reconstruction - PhonemesIPA: " + results["Reconstructed_Voc_Matrix"]["PhonemesIPA"])
            print("Reconstruction - Phonemes: " + results["Reconstructed_Voc_Matrix"]['Phonemes'])
            print("Reconstruction - Phon. Classes: " + results["Reconstructed_Voc_Matrix"]['PhonemeClasses'])
            print("Reconstruction - Stress: " + results["Reconstructed_Voc_Matrix"]['Stress'])
            print("Reconstruction - Vowel Length: " + results["Reconstructed_Voc_Matrix"]['VowelLength'])
            print()
            print("----")
            print()

    else:
        results["Reconstructed_Voc_Matrix"] = None
        results["Reconstructed_Vocalization"] = None



    return results