# How to create a function with data

# Step 1. Function definition
def bnbRefund(accountnumber, refundamount):
    print('refundamount' + 'to there account.')
    print('refund amount: $' + refundamount)

# Step 2. Function call (invocation)
bnbRefund(19292929, 3000) # arguements are real data

# Class Activity 1
# Create a birthday message function.
# Your function should have two parameters;
# 1 for name and the other for birth date.
# Both parameters should be string data types.
# Your function should concatenate the parameters
# with a pre-written strings and form the following message:
# My name is {Beau} and my birthday is {august 31}.

def name_bday(name, bday):
    print('my name is '+ name + ' my bday is ' + bday)

# Birthdate('Dave','December 25th') 

# My {13} dollar(s) is equal to {1300} pennies.

def dollarConverter(dollar):
    pennies = dollar * 100
    print('My '+ str(dollar) + 's is equal 0 to ' + str(pennies) + ' pennies.')

dollarConverter(5)
