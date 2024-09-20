sum=0
no=int(input("Enter a numbe to print Table :"))
for i in range(10,0,-1):
    table=no*i
    print(no,"*",i,"=",table)
    sum = sum + table
print("Sum of Table :",sum)