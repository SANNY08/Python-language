n=int(input("Enter 1st number :"))
n1=int(input("Enter 2nd number :"))
if n>n1:
    samller=n1
else:
    smaller=n
for i in range(1,smaller+1):
    if n%i==0 and n1%i==0:
        hcf=i
lcm=(n*n1)/hcf
print("The Lcm of ",n,'and',n1,'is :',lcm)
print("The HCF of",n,'and',n1,'is :',hcf)
