agetodrive = 17
driverAge = int(input('how old are you?'))

while agetodrive >= driverAge: # 18 > 17 
    print("Sorry you are not old enough to drive yet")
else:
    print("Great you can drive now")


def numberLoop():
   numberInput = input("Please enter a number: ")
    
    

    # print('code is working things are good')

def numberLoop():
    numberLoop = []
    userNumber = ("Type new number")
    print(4,5,6,7)
    while userNumber != 'new number':
        newNumber = int(userNumber)
        numberLoop.sum('start, 4,5,6,7,')





# Create a function
# print out list of numbers based on user input
# user numbers are added to a list
# loop stops when the user enters "quit"

def numberListLoop():
    numberList = []
    userNumber = input("Type in a number: ")
    while userNumber != 'quit':
        newNumber = int(userNumber)
        numberList.append(newNumber)
        print(numberList)
    else:
        print("Loop has stopped. ")

numberListLoop() 



def numberListLoop():
    numberList = []
    userNumber = input("Add a new number")
    while userNumber != 'add':
        newNumber = int(userNumber)
        numberList.sum(numberList)
        print(numberList)
    else:
        print("Number has been added. ")






def numberGuessingGame():
    correctNumber = 7
    userGuess = int(input("Please guess a number: "))
    while userGuess != correctNumber:
            if userGuess > correctNumber:
                print("your guess is too high")
                UserGuess = int(input("Please guess a number: "))
            else:
                print("Your guess is too low ")
                userGuess = int(input("Please guess a number: "))             
    else:
        print("Congrats, you got the correct number! ")

numberGuessingGame()