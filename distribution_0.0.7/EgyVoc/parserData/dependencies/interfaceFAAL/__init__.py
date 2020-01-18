from py4j.java_gateway import JavaGateway, GatewayParameters

def interfaceFAAL(word_A, word_B):


    gateway = JavaGateway()



    addition_app = gateway.entry_point

    aligments = addition_app.addition(word_A, word_B)

    alignmentsResultsItem = {}

    alignmentsResultsItem["bestAlignGlobal"] = aligments[0].getGlobalSimilarityScore()
    alignmentsResultsItem["bestAlignCorrected"] = aligments[0].getCorrectedGlobalSimilarityScore()
    alignmentsResultsItem["wordWithDiacritics_1"] = aligments[0].getWord1_WithDiacritics().replace("\t", "  ")
    alignmentsResultsItem["wordWithoutDiacritics_1"] = aligments[0].getWord1_WithoutDiacritics().replace("\t", "  ")
    alignmentsResultsItem["wordWithDiacritics_2"] = aligments[0].getWord2_WithDiacritics().replace("\t", "  ")
    alignmentsResultsItem["wordWithoutDiacritics_2"] = aligments[0].getWord2_WithoutDiacritics().replace("\t", "  ")


    return alignmentsResultsItem