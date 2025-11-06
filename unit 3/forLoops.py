# For Loops - A type of construct that runs code instructions
# a finite amount of times over a group of data. 

halloweenBag = ['Snickers','Hershey Bar','Twizzler','Candied Apple','Candy corn']

count = len(halloweenBag)

print(count)

# i is a variable and is short for iterator. 
# for i in halloweenBag:
#    print(i)
#    print('I go this candy in my bag ' + i)


# Use a for loop to ask a user to type in 5 words and print each word out in
# the terminal. Once the user has finished typing 5 words, 
# the for loop should end. 

# Clarification: program should ask the user to type in one word. Then the program
# should print it out and ask them to type another word. Your program
# should do this 5 times.

# Create a function that uses a for loop to find the largest number. 
# Your user should be able to type in 5 numbers. 
# Once the user types in 5 numbers your program 
# should be able the find the highest number.

def tf():
    for x in range(3):
        print('true or false: 3 is greater than 2')
        answer = input()
        if answer != 'true':
            print('wrong, try again')
            print('attempt: '+ str(x))
        else:
            print('great!')
            break # stops the loop. regardless of it being a for or while loop


# Hint # 1: you should use the range() function.


# looping through strings
word = " p y t h o n"
for letter in word:
    print(letter)
    if letter == "p":
        print('did you mean paper')
    elif letter == 'y':
        print("did you mean: python")



# looping through lists of numbers
shoppingPrices = [3.00, 5.40, 7.20, 9.00]
total = 0
discount = 10.00
for items in shoppingPrices:
    total += items
    if total > 20.00:
        newTotal = total - discount

print(newTotal)




studentBody = ['a','b','c']
present = []
tardy = []
absent = []
for student in studentBody:
    # if scanned in add to presnt list
    # present.append(student)
    # else add to absent list
    # absent.append(student)
    print('')














