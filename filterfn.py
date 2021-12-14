"""It takes bool returning fn as argument and list as argument"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def checkifdivny2(a):
    return a % 2 == 0


filterlist = list(filter(checkifdivny2, list1))
print(filterlist)
