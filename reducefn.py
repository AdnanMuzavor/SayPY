from functools import reduce

list2 = [1, 2, 3, 4]

"""METHOD-1,long method"""
"""To add all elements of list, i.e to accumulate them"""
s = 0
for item in list2:
    s += item
print(s)

"""Method 2 using reduce"""
sum=reduce(lambda x,y:x+y,list2) #take prev x, add new y, now x+y is prev x so add new y to it and so on
print(sum)
prod=reduce(lambda x,y:x*y,list2) #take prev x, multiply new y, now x*y is prev x so multiply new y to it and so on
print(prod)

