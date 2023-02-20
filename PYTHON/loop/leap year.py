mon=int(input("enter month"))
if mon==2:
    year=int(input("enter year"))
    if (year%4==0) and (not(year%400==0)) or (year%400==0):
        num_days=29
else:
    num_days=28

if mon in [1,3,5,7,8,12]:
    num_days=31

if mon in [4,6,9,11]:
    num_days=29
    
    
print("no of days",num_days,"in month",mon)

