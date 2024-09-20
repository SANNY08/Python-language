n=int(input("Enter 1st number :"))
n1=int(input("Enter 2nd number :"))
for i in range(1,n*n1 +1):
    if (i%n==0 and i%n1==0):
        print("The Lcm of ",n,'and',n1,'is :',i)
        break
