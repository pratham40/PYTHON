num=0
for i in range(1,5):
    num+=1
    for j in range(1,num+1):
        print("*",end=" ")
    print()   

num=5
for i in range(1,4):
    num-=1
    for j in range(1,num):
        print("*",end=" ")
    print()
    
    
#o/p

'''


* 
* * 
* * * 
* * * * 
* * * 
* * 
* 

'''