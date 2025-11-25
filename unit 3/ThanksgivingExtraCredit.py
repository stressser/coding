def letterGrade():
    Grade = int(input('What is your grade?' ))
    A = [] # 90 Score
    B = [] # 80 Score
    C = [] # 70 Score
    D = [] # 60 Score
    F = [] # 50 Score
    Grade = 2025 
    if Grade >= 90:
        print('return "A"')
    elif Grade >= 80:
        print('return "B"')
    elif Grade >= 70:
        print('return "C"')
    elif Grade >= 60:
        print('return "D"')
    else:
        print('return "F"')