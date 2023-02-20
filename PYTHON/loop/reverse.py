rev=0
num=eval(input("enter no"))
while num>0:
    rem=num%10
    rev=rev*10+rem
    num//=10

print("reverse of no",rev)