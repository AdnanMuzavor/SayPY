# Help in making list,dictionaries and geenrators in single line

"""Generating list"""
list1 = [i for i in range(10)]  # List with values till 10 (loop)
print(list1)
list1 = [i for i in range(20) if i % 2 == 0]  # list with loop+conditionals
print(list1)

"""Generating dictionary"""
dict1 = {i: f"item{i}" for i in range(10)}  # dict using only loop
print(dict1)
dict1 = {i: f"item{i}" for i in range(
    20) if i % 3 == 0}  # dict using only loop
print(dict1)
dict2 = {value: key for key, value in dict1.items()}  # using dict1
print(dict2)

"""Generating through list (list vs set)"""

"""generating set ->{}"""
# set1 being set will hv unique elements
set1 = {dress for dress in ["dress1", "dress2", "dress1", "dress2"]}
print(type(set1))
print(set1)

"""generating list ->[]"""
# set1 being list will hv all elements
set1 = [dress for dress in ["dress1", "dress2", "dress1", "dress2"]]
print(type(set1))
print(set1)

"""generating generators ->()"""
gen1 = (i for i in range(10))
print(gen1)
print(gen1.__next__())
print(gen1.__next__())
