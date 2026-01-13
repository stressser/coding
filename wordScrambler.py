import random 

def scramblewordgame():
    wordPool = ['Pennsylvania', 'North Carolina', 'Congregate', 'function']
    print("Welcome to the Word Scrambler Game!")

    randomwordSelect = random.randint(0, 3)
    correctWord = wordPool[0]
    
    if randomwordSelect == 0:
        print(wordPool[0])
        correctWord = wordPool[0]
    elif randomwordSelect == 1:
        print(wordPool[1])
        correctWord = wordPool[1]                            
    elif randomwordSelect == 2:
        print(wordPool[2])
        correctWord = wordPool[2]                           
    elif randomwordSelect == 3:
        print(wordPool[3])
        correctWord = wordPool[3]

        convertedSelection = list(correctWord)
        random.shuffle(convertedSelection)
        scrmabled = "".join(convertedSelection)

        print("Guess the correct Word: " + scrmabled)
        userguess = input()
        if userguess == correctWord:
            print("Congrats! that is correct")
        else:
            print("Sorry, that is incorrect.")
         
scramblewordgame()
