from math import pi
r=eval(input("enter radius"))
if r>0:
    a=pi*r*r
    print("area of circle = ",format(a,".2f"))
    c=2*pi*r
    print("circumference of circle",format(c,".2f"))
