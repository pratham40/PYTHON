n=int(input("enter no"))
flag=True
if n==1:
    print(n,"isnot prime no")
elif n>1:
    for i in range(2,n):
        if n%i ==0:
            flag=False
            break
    if flag:
        print(n,"is prime no")
    else:
        print(n,"is not prime no")

