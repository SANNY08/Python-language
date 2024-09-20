name=input("Enter Consumer Name :")
id=int(input("Enter consumer id :"))
pmr=int(input("Enter PMR :"))
cmr=int(input("Enter CMR :"))
cpu=int(input("Enter CPU :"))
tu=cmr-pmr
eb=tu*cpu
print("consumer Name :",name)
print("Consumer id :",id)
print("Total unit is :",tu)
print("Electricity Bill :",eb)