print("$$$$$$$$calculator$$$$$$$$$$")
print("\n")
num1=float(input("enter first no"))
num2=float(input("enter second no"))
print("enter 1 for 'addition'\nenter 2 for 'subtraction' \nenter 3 for 'multiplication' \nenter 4 for 'division' \nenter 5 for 'power' \nenter 6 for 'floor'\n enter 7 for 'modulus'")
enter_choice=int(input("enter choice b/w 1 to 7"))
if enter_choice==1:
    print("addition:",num1+num2)
    
elif enter_choice==2:
    print("subtraction:",num1-num2)
    
elif enter_choice==3:
    print("multiplication:",num1*num2)
    
elif enter_choice==4:
    print("division:",num1/num2)
    
elif enter_choice==5:
    print("power:",num1**num2)
    
elif enter_choice==6:
    print("floor:",num1//num2)
    
elif enter_choice==7:
    print("modulus:",num1%num2)
    
else:
    print("invalid choice")