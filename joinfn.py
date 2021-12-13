list = ["harry", "parry", "carry", "varry"]
for item in list:
    print(item, " and", end=" ")
print("Other ppl.")

"""Doing same with help of join"""
a = " and ".join(list)  # Join each element of list with " and "
print(a, " and other ppl.")

"""Doing same with help of join"""
b = " , ".join(list)  # Join each element of list with " and "
print(b, " and other ppl.")
