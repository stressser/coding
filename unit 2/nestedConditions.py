def atm():

    balance = 5000
    pin = 1234

    print("welcome, please type in your pin number: ")
    userPin = int(input())

    if (userPin == pin):
        print("welcome what would you like to do? ")
        print("1. Withdraw money")
        print("2. Deposit money")
        print("3. Check balance")
        select = int(input("pleae select an option: "))
        if select == 1:
            print('How much would you like to withdraw? ')
            amount = int(input())
            if amount > balance:
                print("Overdraft alert")
            else:
                newBalance = balance -amount 
                print("You are taking out: " + str(amount))
                print("You have this amount left: " + str(newBalance))

        elif select == 2:
            print('How much would you like to deposit? ')
            amount = int(input())
            
        elif select == 3:
            print(" you are taking out: " + str(amount))

        else:
            print("Sorry dont understand your selection")

    else:
        print("Pin is incorrect.")
        atm()

atm()


# Python Lists = a way to organize data, regardless of data type.

# List Syntax - create a varible and then assign it to square brackets.
# write the data you want in your list in the square brackets.

groceries = ['words', 19, 12.3, True, 'new words']