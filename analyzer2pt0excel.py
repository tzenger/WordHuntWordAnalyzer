import copy
with open("officialdic.txt", "r") as file:
    words = file.read().splitlines()
maxLength = 4 # Maximum length of word which would be considered while the program runs


class letterCombo():
    letters = ""
    words = []
    count = 0
    def __init__(self, letters, words):
        self.letters = letters
        self.words = words

    def setLetters(self, newLetters):
        self.letters = newLetters

    def addWord(self, newWord):
        self.words.append(newWord)

    def addWordList(self, newWordList):
        for word in newWordList:
            self.words.append(word)
        
    def setCount(self):
        self.count = len(self.words)

    def __str__(self):
        return self.letters + " can turn into " + ", ".join(self.words) + " Count: " + str(self.count)

class alphWord():
    orgWord = ""
    alphWord = ""
    def __init__(self, orgWord):
        self.orgWord = orgWord
        self.alphWord = alphabetize(orgWord)

    def returnOrgWord(self):
        return self.orgWord

    def returnAlphWord(self):
        return self.alphWord

    def __str__(self):
        return self.orgWord + " " + self.alphWord

def alphabetize(word): # Alphabetizes the letters in the word (Ex. EAT turns to AET)
    wordLetters = list(word)
    wordLetters.sort()
    alphWord = ""
    for x in wordLetters:
        alphWord += x
    return alphWord

def reSort(LCL):
    for letterCombo in LCL:
        letterCombo.words.sort()
        letterCombo.words.sort(key=len, reverse=True)

def createAWL(WL): # Creates an alphWordList
    alphWordList = []
    for word in WL:
        alphWordList.append(alphWord(word)) # Makes the original list into a list of alphWord Objects
    alphWordList.sort(key=lambda x: x.alphWord) # Sorts the alphWordList by alphabetical order with regard to alphWord
    return alphWordList

def createLCL(AWL): # Creates a letterComboList
    currAlphWord = AWL[0].alphWord # Presetting before the for-loop
    letterComboList = []
    letterComboList.append(letterCombo(currAlphWord, []))
    LCLIndex = 0 # Index of the LetterComboList to be used
    for word in AWL:
        if currAlphWord != word.alphWord: # If the alphWord being checked is not the currently running alphWord
            currAlphWord = word.alphWord # It becomes the new alphWord
            letterComboList[LCLIndex].setCount() # Sets the count of the letterCombo object which is no longer going to be used
            LCLIndex += 1 # Increments the LCLIndex
            letterComboList.append(letterCombo(word.alphWord, [])) # A new letterCombo object is created using the new alphWord and is appended onto the LCL
            letterComboList[LCLIndex].addWord(word.orgWord) # Adds the word that had the new alphWord to the word list of the new letterCombo object
            letterComboList[LCLIndex].setCount()
        else:
            letterComboList[LCLIndex].addWord(word.orgWord) #If == alphWord, then it adds the word associated with the alphWord to the list of words in the letterCombo Object
    letterComboList.sort(key=lambda x: x.count, reverse=True)
    return letterComboList

def LCCCMerger(LCCCtemp): # Merges all the LCLs in the LCCC into one LCL with word length maxLength
    test = True
    for x in range(2, maxLength + 1):
        if len(LCCCtemp[x]) != 0:
            for letterCombo in LCCCtemp[x-1]:
                for letterComboUp in LCCCtemp[x]:
                    charList = list(letterCombo.letters)
                    charListUp = list(letterComboUp.letters)
                    test = True
                    for char in charList:
                        if char in charListUp:
                            charListUp.remove(char)
                        else:
                            test = False
                            break
                    if test:
                        letterComboUp.addWordList(letterCombo.words)
                        letterComboUp.setCount()
    LCCCtemp[maxLength].sort(key=lambda x: x.count, reverse = True)
    for LCL in LCCCtemp:
        reSort(LCL)
    return LCCCtemp[maxLength]


# Start of the actual running ----------------------
wordList = words

LCCC = [] #Letter Combo Character Counted: an array where words of the same length are sectioned off into their own lists, contained in the LCCC
for x in range(0, maxLength + 1): # Length of words 
    tempList = []
    for word in wordList:
        if len(word) == x:
            tempList.append(word)
     #It doesn't display all the items, but they are all there. Hopefully lol
    if len(tempList) != 0:
        LCCC.append(createLCL(createAWL(tempList)))
    else:
        LCCC.append([])
LCCC[2] = [] # 2 Letter Words are not counted in Word Hunt
#L3 = copy.deepcopy(LCCC[3])
#L4 = copy.deepcopy(LCCC[4])
#L5 = copy.deepcopy(LCCC[5])
finalLCL = LCCCMerger(LCCC)








# Writing to an excel Spreadsheet ------------------------

import xlwt 
from xlwt import Workbook
# Workbook is created 
wb = Workbook() 

sheet1 = wb.add_sheet('3-5 Letters', cell_overwrite_ok=True)
sheet2 = wb.add_sheet('3 Letters', cell_overwrite_ok=True)
sheet3 = wb.add_sheet('4 Letters', cell_overwrite_ok=True)
sheet4 = wb.add_sheet('5 Letters', cell_overwrite_ok=True)

sheet1.write(0, 0, "Combo")
sheet1.write(0, 1, "Count")
sheet1.write(0, 2, "Words")
sheet2.write(0, 0, "Combo")
sheet2.write(0, 1, "Count")
sheet2.write(0, 2, "Words")
sheet3.write(0, 0, "Combo")
sheet3.write(0, 1, "Count")
sheet3.write(0, 2, "Words")
sheet4.write(0, 0, "Combo")
sheet4.write(0, 1, "Count")
sheet4.write(0, 2, "Words")

for x in range(0, len(finalLCL)):
    for y in range(0, len(finalLCL[x].words)):
        sheet1.write(x + 1, 0, finalLCL[x].words[0])
        sheet1.write(x + 1, 1, finalLCL[x].count)
        sheet1.write(x + 1, y + 2, finalLCL[x].words[y])
"""
for x in range(0, len(L3)):
    for y in range(0, len(L3[x].words)):
        sheet2.write(x + 1, 0, L3[x].words[0])
        sheet2.write(x + 1, 1, L3[x].count)
        sheet2.write(x + 1, y + 2, L3[x].words[y])

for x in range(0, len(L4)):
    for y in range(0, len(L4[x].words)):
        sheet3.write(x + 1, 0, L4[x].words[0])
        sheet3.write(x + 1, 1, L4[x].count)
        sheet3.write(x + 1, y + 2, L4[x].words[y])


for x in range(0, len(L5)):
    for y in range(0, len(L5[x].words)):
        sheet4.write(x + 1, 0, L5[x].words[0])
        sheet4.write(x + 1, 1, L5[x].count)
        sheet4.write(x + 1, y + 2, L5[x].words[y])
"""

wb.save('threeToFourLetter.xls') 