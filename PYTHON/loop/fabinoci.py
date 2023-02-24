n1=int(input("enter no1"))
n2=int(input("enter no2"))
l=int(input("enter limit"))
print(n1,end=" ")
print(n2,end=" ")

for i in range(l+1):
    sum=n1+n2
    n1=n2
    n2=sum
    print(sum,end=" ")