name = input('Enter user name....')


def ask_gender() -> str:
    return str(input("Enter your Gender: ")).lower()


valid_genders = ["male", "female"]
gender = None

gender = ask_gender()
while gender not in valid_genders:
    print("Unknown gender, try again")
    gender = ask_gender()

print(f"You have chosen {gender}")
import re


def isValid(s):
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")

    return Pattern.match(s)


s = input('Enter a valid mobile no.  :')


def isValid(s):
    Pattern = re.compile("(0|91)?[1-9][0-9]{9}")

    return Pattern.match(s)


p = input('Enter a valid Consumer no..  :')

a = input('Previous Month Meter  reading -  ')
a1 = input('Current Month Meter Reading   -  ')
TotalUnit = int(a1) - int(a)

if (TotalUnit <= 100):
    Bill = TotalUnit * 7
elif (TotalUnit <= 200):
    Bill = TotalUnit * 7.5
elif (TotalUnit <= 300):
    Bill = TotalUnit * 8
else:
    Bill = 0
print('Consumer Name   : ', name)
if (isValid(s)):

    print("Valid Number")
    print('Mobile no.   :', s)

else:

    print("Invalid  = consumer Number")
if (isValid(p)):

    print('Consumer no.   :', p)

else:

    print("Invalid  =  Consumer no.")
print('Total Unit Consumed  ::', TotalUnit)
print('TotalAmout   =', Bill)