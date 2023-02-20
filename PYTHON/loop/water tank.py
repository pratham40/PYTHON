from math import pi
h=10
r=5
f=15
t=eval(input("enter time"))
vtank=pi*pow(r,2)*h
vwater=f*t
if vtank<vwater:
    print("overflow",vwater-vtank)
elif vtank>vwater:
    print("underflow")
    ht=vwater/pi*r**2
    hr=h-ht
    print(f"filled height={ht},remaining height={hr}")
else:
    print("tank full")
10