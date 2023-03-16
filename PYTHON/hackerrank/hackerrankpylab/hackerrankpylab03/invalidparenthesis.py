# Enter your code here. Read input from STDIN. Print output to STDOUT

count=0
for ch in input():
    if ch=='(':
        count+=1
    else:
        count-=1
        if count<0:
            break
            
print(f"'{count==0}'")