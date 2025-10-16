# while Loop definition - a while loop is a type of construct
# where code instructions will kep on running so
# long as a condition is TRUE (boolean)

# NOTE - In order to stop a loop (or any program) from running
# in your terminal, click crtl + c at the same time.

# While Loop Syntax

ageToBuyGame = 17
customerAge = int(input('how old are you: '))

while ageToBuyGame >= customerAge: # 17 > 15
    print("Sorry, you are not old enough to buy GTA VI")
else:
    print("great enjoy your collecters edition of GTA VI.")



savedPassword = '123Abc'
userPassword = input("please type in your password: ")
attempt = 1
while savedPassword != userPassword: #123Abc != 123Abc
      print("Incorrect try again please.")
      attempt +=1
      userPassword = input("Pleast type in your password again: ")
      if attempt ==3:
           print('Sorry, your account has been locked. Please wait 5 minutes.')
           break
else:
     print("welcome to your account.")