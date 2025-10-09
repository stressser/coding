# Question 1

def agetovote(age):
    if age >= 18:
        print("Allowed to vote.")
    else:
        print("sorry not old enough to vote.")
        
# votingAgecheck (67)

# Question 2

def maxNumber():
    a = input("please enter your first number: ")
    b = input("please enter your second number: ")
    c = input("please enter your third number: ")
    hiNumber = max(a,b,c)
    print(hiNumber) 

# maxNumber()


# Question 3


def movieTicket():
    age = int(input("how old are you? "))
    if age <=13:
        print('Your ticket is $10.00')
    elif age >=14:
        print("Your ticket is $15.00")
    elif age >= 25:
        print('Your ticket is $20.00')
    else:
        print('Your ticket is $10.00')

movieTicket()