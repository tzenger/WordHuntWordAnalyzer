with open("combined.txt", "r") as file:
    words = file.read()

wordList = words.split(" ")

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

    def setCount(self):
        self.count = len(self.words)

    def show(self):
        print("Letter Combo: " + self.letters + " \tCount: " + str(len(words)))
        for x in range(0, len(words)):
            print(self.words[x])

    def __str__(self):
        return self.letters + " can turn into " + ", ".join(self.words) + " Count: " + str(self.count)

def alphabetize(word):
    wordLetters = list(word)
    wordLetters.sort()
    alphWord = ""
    for x in wordLetters:
        alphWord += x
    return alphWord

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

    #def show(self):
      #  print(self.orgWord + " " + self.alphWord)

    def __str__(self):
        return self.orgWord + " " + self.alphWord


#print(alphabetize("mid"))

alphWordList = []
for word in wordList:
    alphWordList.append(alphWord(word))
#print(*alphWordList, sep = "\n")

alphWordList.sort(key=lambda x: x.alphWord) # Sorts the alphWordList by alphabetical order with regard to alphWord
#print(*alphWordList, sep = "\n")


currAlphWord = alphWordList[0].alphWord
#print(*alphWordList, sep = "\n")
letterComboList = []
letterComboList.append(letterCombo(currAlphWord, []))
LCLIndex = 0
for word in alphWordList:
    if currAlphWord != word.alphWord:
        currAlphWord = word.alphWord
        letterComboList.append(letterCombo(word.alphWord, []))
        letterComboList[LCLIndex].setCount()
        LCLIndex += 1
        letterComboList[LCLIndex].addWord(word.orgWord)
        #print(str(LCLIndex) + ": " + str(letterComboList[LCLIndex]))
    else:
        
        letterComboList[LCLIndex].addWord(word.orgWord)
        #print(str(LCLIndex) + ": " + str(letterComboList[LCLIndex]))
        
print()
#print(*letterComboList, sep = "\n")
letterComboList.sort(key=lambda x: x.count)
print(*letterComboList, sep = "\n")