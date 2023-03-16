st=input()
re=''
if len(st)%2:
    print('Odd length. ')
else:
    for i in range(0,len(st),2):
        re+=st[i+1] + st[i]
    print(re)