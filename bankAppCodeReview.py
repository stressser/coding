def payCheckFilter(payRate, hours, daysWorked):
    checkingAccount = 50
    retirementAccount = 25
    savingsAccount = 25

    paycheck = payRate * hours * daysWorked
    print('My pay check for working '+ str(daysWorked) + ' day(s) will be ' + str(paycheck))

    print('Checking Account Deposit: ' + str(paycheck * (checkingAccount / 100)))
    print('Retirement Account Deposit: ' + str(paycheck * (retirementAccount /100)))
    print('Savings Account Deposit: ' + str(paycheck * (savingsAccount / 100)))

payCheckFilter(10.00, 5, 7)