num=int(input("enter no"))
x=num
sum=0
while num>0:
    rem=num%10
    sum=sum+rem*rem*rem
    num//=10
if(x==sum):
    print("armstrong no")
else:
    print("not armsttrong no")
