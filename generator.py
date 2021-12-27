"""Generators generate value on fly i.e they generate value as we run next fn on generator object else it does't"""


def fecto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fecto(n-1)

# generator capable of generating vales till n-1


def gen(n):
    for i in range(n):
        yield i

# generator generating factorial vals in fectorial


def fectgen(n):
    for i in range(n):
        yield f"factorail of {i} is {fecto(i)}"


# making generator object
g = gen(5)
print(g)  # Will print that it's type of generator
print(g.__next__())  # This will start generator
print(g.__next__())  # This will print next value of generator

"""Generating all values at once"""
for i in g:
    print(i)

# Generating fectorial values
f = fectgen(5)
print(f)
print(f.__next__())
print(f.__next__())
for i in f:
    print(i)
