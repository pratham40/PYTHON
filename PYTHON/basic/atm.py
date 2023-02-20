amt=eval(input("enter amount"))
amt-=100
_2k_=amt//2000
amt%=2000    # amt=amt-_2k_*2000
fiveh=amt//500
amt%=500
twoh=amt//200
amt%=200
oneh=amt//100+1

print(f'no of 100 notes{oneh}')
print(f'no of 200 notes{twoh}')
print(f'no of 500 notes{fiveh}')
print(f'no of 2000 notes{_2k_}')