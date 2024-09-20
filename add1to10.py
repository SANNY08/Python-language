def add(n):
    if n==1:
        return 1
    else:
        return n+add(n-1)
r=add(10)
print("Sum is :",r)