"""Else with loop is executed omly when loop comes to an end"""
"""Use mainly to print statement to be printed at end of loop"""

list = ["123", "234", "345", "456"]

# example-1
for item in list:
    print(item)
else:
    print("List executed till end")

# example-2
for item in list:
    if item == "123":
        print(item)
        break
else:
    print("Item not found")

# example-2
for item in list:
    if item == "567":
        break
else:
    print("Item not found")
