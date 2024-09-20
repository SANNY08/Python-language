a=int(input("Enter First side  :"))
b=int(input("Enter Second side :"))
c=int(input("Enter Third side  :"))
s=(a+b+c)            #calculate the perimeter
p=s/2                     #CLACULATE HALF-PERIMETER
area=(s*(s-a)*(s-b)*(s-c)) **0.5  #calculate the area
print("Area of Triangle is  =",area)
print("Perimeter of Triangle is =",s)
print("Half-Perimeter of Triangle is =",p)


