# Function- is a set of code instructions labeld under
# a custom name that  the computer will run.

# Function Syntax (rules of how its written)
# functions have 2 phases: function definition and
# function call

# phase 1: function definition
# we are describing the instruction for our custom code
# we are adding logic to the computers vocabulary.
# this code does not run- it only gives the computer the meaning
# not the action

def example():
     print('good morning.') # 1 instruction: print good morning

# phase 2: function call
# once we have the definition, we can now run the instructions
# by writing the function name.
example()

# we indent to inform the computer that we are about to write
# code instructions. if we dont, we will get an error

def example2():
      print('good day')
     a = input('enter a number: ')
     print(a)

def math():
    a = input("Please enter a number:")
    b = 30
    print("here is your resuly!")
    print(int(a) + b)

# Create a function that calculated 2 unique user inputted numbers

def calculate():
    a = input('Please enter a number: ')
    b = input('Please enter another number: ')
     print(int(a) + b)
     print(int(a) - b)
     print(int(a) / b)
     print(int(a) * b)
     
calculate()