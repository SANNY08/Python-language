name=input("Enter emp_Name :")
bs=int(input("Enter Basic salary :"))
ta=float(bs*10)/100
da=float(bs*20)/100
hra=float(bs*30)/100
net=float(bs+ta+da+hra)
print("Employee name :",name)
print("Net Salary =",net)