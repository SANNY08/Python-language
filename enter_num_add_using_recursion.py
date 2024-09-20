def add(n):
    if n==1:
        return 1
    else:
        return n+add(n-1)
x=int(input("Enter a number :"))
r=add(x)
print("Sum is :",r)