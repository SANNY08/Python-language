n=float(input("Enter Unit :"))
if n<=100:
    print("No charge")
elif n>100 and n<=200:
    print("Your bill is :",(n-100)*5)
elif n>200:
    print("Your bill is :", 500+(n - 200)*10)
    