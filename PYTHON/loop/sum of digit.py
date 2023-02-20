sum=0
num=eval(input("enter no"))
while num>0:
    rem=num%10
    sum+=rem
    num//=10
print("sum of digit",sum)