sample = ["2", "3", "4"]
print(sample)
"""doing sample[0]+=1 will will an error as elements are string"""

# Method-1
for i in range(len(sample)):
    sample[i] = int(sample[i])

print(sample)
print(sample[0]+sample[2])  # possible as now nos are int

# Method-2 using map
"""  map(fn-name to be applied on each element of sample,sample)"""

sample2 = ["1", "3", "5"]

""" fn passed->integer fn"""
print(map(int, sample2))  # returns map object
# sample(map-obj) converts it to sample-type
intsample2 = list(map(int, sample2))
print(intsample2)

"""making a fn and passing it"""


def fn(a):
    return a*a


sample3 = list(map(fn, intsample2))
print(sample3)

"""using lambda fn instead"""

sample4 = list(map(lambda x: x*x*x, intsample2))
print(sample4)

"""High level application"""


def square(a):
    return a*a


def cube(a):
    return a*a*a


fnlist = [square, cube]

for i in range(5):
    val = list(map(lambda x: x(i), fnlist))
    # val=x(0) i.e square(0),cube(0) i.e [0,0]
    # val=x(2) i.e square(2),cube(2) i.e [4,8]
    print(val)
