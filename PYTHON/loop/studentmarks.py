n=eval(input("enter how many students"))
for  i in range(1,n+1):
    print(i,"st students marks")
    m=int(input("enter maths marks"))
    e=int(input("enter english marks"))
    h=int(input("enter hindi marks"))
    s=int(input("enter science marks"))
    sst=int(input("enter sst marks"))
    t=m+e+h+s+sst
    g=t/5
    if (g>90):
        print("A+")
    if (85<g<=90):
        print("A")
    if (80<g<=85):
        print("B+")
    if (75<g<=80):
        print("B")
    if(g<75):
        print("average")
    
    