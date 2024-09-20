bs=int(input("Enter your basicc salary :"))
if bs<20000:
    ta = (bs * 10) / 100
    da = (bs * 20) / 100
    hra = (bs * 30) / 100
    s=float(ta+da+hra)
    net=float(ta+da+hra+bs)
    print("Total ta,da,hra is :", s)
    print("Net salary :",net)
elif bs>=20000:
    ta=(bs*20)/100
    da=(bs*30)/100
    hra=(bs*40)/100
    s = float(ta + da + hra)
    net = float(ta + da + hra + bs)
    print("Total ta,da,hra is :", s)
    print("Net salary :", net)



