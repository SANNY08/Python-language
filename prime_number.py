no=int(input("Enter a number :"))
count=0
for i in range(1,no+1,1):
    if no%i==0:
        count=count+1
if count==2:
    print("Number is Prime")
else :
    print("Number is Not Prime")