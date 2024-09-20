no=int(input("Enter the value of x :"))
no2=int(input("Enter the value of y :"))
arth=input("Select Any Arthematic Operator (+,-,*,/,%).")
p=no+no2
p1=no-no2
p2=no*no2
p3=no%no2
p4=no/no2
if arth=='+':
    print("Sum of two number is :",p)
elif arth=='-':
    print("Substractio of two Number :", p1)
elif arth=='*':
    print("Multiplication of two Number :", p2)
elif arth=='/':
    print("Divide of two Number :", p4)
elif arth=='%':
    print("Remender of two Number :", p3)
else:
    print("\nYOU ENTERED WRONG ARTHEMATIC OPERATOR !\nPLEASE CHOOSE IN THIS BRACKET SYMBOL(+,-,*,/,%)")
