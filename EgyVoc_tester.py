from EgyVoc import EgyVoc
from EgyVoc import initializeFAAL

#initialize the FAAl aligning algorithm - note: the java program needs to be shut down and initialized again at every new run
initializeFAAL()

# Test 1: reconstruct vocalization on the basis of Coptic

print ()
print ("- - - - - -")
print ("-- Test 1 --")
print ()

#Coptic word:
SahidicFormToParse = "ϩⲓⲃⲱⲓ"

#Parse data:
results = EgyVoc(\
    SahidicWord = SahidicFormToParse, \
    verbose = True\
    )

print("Results as a Python Dictionary:")
print (results)

# Test 2: reconstruct vocalization on the basis of Coptic and the Egyptian Consonantal root

print ()
print ("- - - - - -")
print ("-- Test 2 --")
print ()

#Print results in the console
verbose = True

#Coptic word:
SahidicFormToParse = "ⲥⲱⲧⲙ"

#Egyptian root:
EgyptianRootToParse = "sḏm"

#Parse data:
results = EgyVoc(\
    SahidicWord = SahidicFormToParse, \
    EgyptianRoot = EgyptianRootToParse,\
    verbose = True\
    )
print("Results as a Python Dictionary:")
print (results)

# Test 3: reconstruct vocalization on the basis of the Group Writing Spellings

print ()
print ("- - - - - -")
print ("-- Test 3 --")
print ()

#Print results in the console
verbose = True

#Group Writing:
GroupWriting = {}
GW_Period_1 = "yA.mA"
GW_Period_2 = "yA.mA"
GW_Period_3 = "yU.mA"
GW_Period_4 = "yU.mA"

#Parse data:
results = EgyVoc(\
    GW_Period_1 = GW_Period_1, \
    GW_Period_2 = GW_Period_2, \
    GW_Period_3 = GW_Period_3, \
    GW_Period_4 = GW_Period_4, \
    verbose = True)

print ("Results as a Python Dictionary:")
print (results)

# Test 4: reconstruct vocalization on the basis of Coptic and selected Group Writing Spellings

print ()
print ("- - - - - -")
print ("-- Test 4 --")
print ()

#Print results in the console
verbose = True

#Coptic word:
SahidicFormToParse = "ϫⲁϫ"

#Group Writing:
GroupWriting = {}
GW_Period_1 = ""
GW_Period_2 = "ṯU.ṯU"
GW_Period_3 = "ṯA.ṯA"
GW_Period_4 = ""

#Parse data:
results = EgyVoc(\
    SahidicWord = SahidicFormToParse, \
    GW_Period_1 = GW_Period_1, \
    GW_Period_2 = GW_Period_2, \
    GW_Period_3 = GW_Period_3, \
    GW_Period_4 = GW_Period_4, \
    verbose = True)

print ("Results as a Python Dictionary:")
print (results)


#terminateFAAL(process)