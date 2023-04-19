# String Subsequences Combinations
s,n=input().split()
n=int(n)
l=len(s)
ls=[]
for i in range(l):
    for j in range(i,l):
        ls.append(''.join(sorted(s[i]+s[j])))
ls.sort()
print(*ls,sep="\n")
