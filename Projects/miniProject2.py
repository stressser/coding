def gpaCalculator():
    gpa = 3.0
    print('Enter the subject to calculate GPA:')
    print('1. Mathematics')
    print('2. English')
    print('3. Science')
    print('4. History')
    print('what subject is the GPA for?')
    subject = input()
    print('the subject is '+ subject)
    week = 1
    print('what is the grade for week '+ str(week))
    for week in range(17):
        grade = input()
        print('the grade for week '+ str(week) + ' is ' + grade)
        week += 1
    gpaCalculator = input('')
    if gpaCalculator == '1':
        print('You have selected Math. Your current GPA is 3.5')
    elif gpaCalculator == '2':
        print('You have selected English. Your current GPA is 3.2')
    elif gpaCalculator == '3':
        print('You have selected Science. Your current GPA is 3.8')
    elif gpaCalculator == '4':
        print('You have selected History. Your current GPA is 2.9')
    else:
        print('Your overall GPA is 0.7')
    
gpaCalculator()