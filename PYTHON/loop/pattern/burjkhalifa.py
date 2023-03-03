n=eval(input())
l=len(bin(n))-2
for i in range(0,n+1):
        k=bin(i)[2:]
        p=len(k)
        print(' '*(l-p)+k)