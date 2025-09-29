# Conditional statements = code that has a set of different
# outcomes based on the data that is given.

# conditional syntax = if / else
# If = the condition we are looking to satisfy
# Else = the default / exit. the thing that happens
# when our condition is NOT satisfied.
weather = input("Whtas the weather like today ?")

if weather == 'sunny':
    print("its gonna be nice out. wear shades.")
else:
    print("Have a good day")

if (weather == 'sunny'):
    print("Its gonna be nice out. Wear shades.")
elif (weather == 'rainy'):

# create a conditional block of code that acts as a password
# checker. The user should be able to input a password.
# If it is correct, they should get a message 
# saying "welcome, you are logged in". 
# Otherwise, they should get a message saying "try again".



# Tell me what to do on each down based on yards.
down = input
yards = input

if down == 3 and yards == 2:
    print("run the ball!")
elif down == 2 and yards < 0:
    print('')
elif down == 3 and yards < 0:
    print('')
else: # this is the exit; assumes it is 4th down.
    print("punt")



age = input('How old is the person? ')
def permitCheck(age):
    if age >= 16:
        print("congrats, you can begin learning to drive.")
    else:
        print("Sorry, your not olf enough yet")

permitCheck(16)

