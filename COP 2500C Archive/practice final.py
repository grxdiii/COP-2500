# gradi

def b1Speak(sentence):

    wordList = sentence.split(".")

    newList = []
    for x in range(len(wordList)-1):
        printing = wordList[x] + ". Rogger Roger. "
        printing = printing.strip()
        newList.append(printing)

    for x in range(len(newList)):
        print(newList[x], end=" ")
    

userInput = "This is the last class. Have a great break."
b1Speak(userInput)


