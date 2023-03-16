st=input()
node=int(input())
rp=int(input())

re1=st[node:] + st[:node]
re2=re1.replace(' ','')*rp

print(*re2)  #unpacking the elements