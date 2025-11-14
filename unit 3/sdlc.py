# 1. We can make it safer = Add authentication,
# Add age limit> Make 2 different variations based on age.
# option 1- Add more ways to verify people
# option 2- Make a different version of tiktok

def signup():
    dob = int(input('what year were you born? '))
    tiktok_kids = [] # 8 - 12 is kids
    tiktok_teens = [] # 13 - 18 is teen
    tiktok_standard = [] # 19 > is adult
    currntYr = 2025
    usrAge = currntYr - dob
    if usrAge < 8 :
        print('welcome to tiktok kids')
        tiktok_kids.append(usrAge)
    elif usrAge > 12 < 18:
        print('wassup chat, wlcome to tik tok teens, 67!')
        tiktok_teens.append(usrAge)
    else:
        print('welcome to tiktok')
        tiktok_standard.append(usrAge)
signup()


'1. Be able to divide'


