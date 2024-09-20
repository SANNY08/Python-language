name=input("Enter Consumer Name :")
id=int(input("Enter consumer id :"))
age=int(input("Enter your age :"))
gen=input("Enter your gender :") #gen=gender
if age>=60:
    pmr = int(input("Enter PMR :"))
    cmr = int(input("Enter CMR :"))
    tu = cmr - pmr
    eb = tu * 3
elif age<60:
    pmr = int(input("Enter PMR :"))
    cmr = int(input("Enter CMR :"))
    tu = cmr - pmr
    eb = tu * 5

print("consumer Name :",name)
print("Consumer id :",id)
print("Your age :",age)
print("You are ",gen)
print("Total unit is :",tu)
print("Electricity Bill :",eb)