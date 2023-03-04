''' hash() is one of the functions in the __builtins__ module,\n
so it need not be imported.
'''

n=int(input())
tup=tuple(map(int,input().split()))
print(hash(tup))