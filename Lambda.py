# Normal function

def minus(a, b):
    return a-b


print(minus(5, 3))

# Lambda function


def plus(a, b): return a+b


print(plus(5, 3))

list1 = [[15, 2], [6, 4], [1, 0]]
"""Automatic sorting"""
# list1.sort()
# print(list1)

"""Sorting my giving key"""
"""Making k"""
# ->Key takes in fn as argument,so using lamda fn, this statement means we want sort fn to sort list based on first val in sublist
list1.sort(key=lambda list: list[0])
print(list1)

# ->Key takes in fn as argument,so using lamda fn, this statement means we want sort fn to sort list based on second val in sublist

list1.sort(key=lambda list: list[1])
print(list1)
