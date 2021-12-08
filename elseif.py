
# else if error
var3=10
var1 = input()
var2 = input()
var1 = int(var1)
var2 = int(var2)
if var1 < var2 and var1==var3:
    print(var1, "<", var2)
elif var1 == var2:
    print(var1, "=", var2)
else:
    print(var1, ">", var2)

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 8, 10, 12]
var4 = input()
var4 = int(var4)

#Using in keyword(returns bool)
if var4 in list1:
    print(var4, "found in", list1)
else:
    print(var4, "not found")

#Using not in keyword(returns bool)
if var4 not in list2:
    print(var4, "not found in", list2)
else:
    print(var4, " found")
