from os import *
from sys import *
from collections import *
from math import *

def printPatt(n):
    for i in range(1, n+1, 1):
        for j in range(1,n-i+2,1):        
            if(i%2!=0):
                print('1', end ='')
            
            else:
                print('0', end ='')
    
        print()


n=input()
printPatt(int(n))


