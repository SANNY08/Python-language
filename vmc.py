ch = input("Please Enter Your Own Character : ")

if (ch.isdigit()):
    print("The Given Character ", ch, "is a Digit")
elif (ch.isalpha()):
    print("The Given Character ", ch, "is an Alphabet")

else:
    print("The Given Character ", ch, "is Not an Alphabet or a Digit")
if ch in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a vowel." % ch)
elif ch == 'y':
    print("Sometimes the letter y stands for a vowel, sometimes for a consonant.")
else:
    print("%s is a consonant."%ch)