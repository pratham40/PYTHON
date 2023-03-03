# A counter is a container that stores elements as dictionary keys,\n
# and their counts are stored as dictionary values.
# from collection import counter
"""
from collections import Counter
mylist=[1,2,3,4,5,1,2,3,4,5]
print(Counter (mylist))
print(Counter(mylist).items())
print(Counter(mylist).values())
print(Counter(mylist).keys())"""

# Counter({1: 2, 2: 2, 3: 2, 4: 2, 5: 2})
# dict_items([(1, 2), (2, 2), (3, 2), (4, 2), (5, 2)])
# dict_values([2, 2, 2, 2, 2])
# dict_keys([1, 2, 3, 4, 5])

'''shoes size
'''

x=int(input())
shoe_size=list(map(int,input().split()))
n=int(input())
sell=0                         #sell
for k in range(n):
    s,p=map(int,input().split())
    if s in shoe_size:
        sell+=p
        shoe_size.remove(s)
print(sell)