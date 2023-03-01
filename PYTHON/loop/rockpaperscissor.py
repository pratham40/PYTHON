name1=input()
name2=input()
ch1=input()
ch2=input()
if ch1=='Rock':
    if ch2=="Scissor":
        print(name1,"Win")
    else:
        print(name2,"Win")

elif ch1=="Scissor":
    if ch2=="Paper":
        print(name1,"Win")
    else:
        print(name2,"Win")


elif ch1=="Paper":
    if ch2=="Rock":
        print(name1,"Win")
    else:
        print(name2,"Win")
