def pythonQuiz():
    grade = 0
    print('1. Which of the following is not a data type? ')
    print("A. Function")
    print("B. Interger")
    print("C. Float")
    print("D. String")
    userAnswer = input('')
    correctAnswer = 'A'
    if userAnswer == correctAnswer:
        grade += 1
        print('Correct')
    else:
        print('Incorrect')
   