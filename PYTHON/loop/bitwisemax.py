n1,n2=map(int,input().split())
k=eval(input())
max=0
a=n1&n2
b=n1|n2
c=n1^n2
if (a>max) and (a<=k):
    max=a
elif (b>max) and (b<=k):
    max=b
elif(c>max) and (c<=k):
    max=c
print(max)


# P=eval(input())
# X=eval(input())
# for  i in range(0,100):
#     for j in range(0,100):
#         if i+j==P and i^j==X:
#             print(i and j)
#             break

# name1=input()
# name2=input()
# ch1=input()
# ch2=input()
# if ch1=='Rock' and ch2=='Scissor':
#     print(name1,"Win")
# else:
#      print(name2,"Win")