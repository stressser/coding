def gpaCalculator():
    gpa = 3.0
    print('Enter the subject you want to enter to see your gpa')
    print('1. Mathematics')
    print('2. English')
    print('3. Science')
    print('4. History')
    gpaCalculator = input('')
    if gpaCalculator == '1':
        print('You selected Math. Your current GPA is 3.5')
    elif gpaCalculator == '2':
        print('You have selected English. Your current GPA is 3.2')
    elif gpaCalculator == '3':
        print('You have selected Science. Your current GPA is 3.8')
    elif gpaCalculator == '4;':
        print('You have selected History. Your current GPA is 2.9')
    else:
        print('Your overall GPA is 0.7')
    
gpaCalculator()