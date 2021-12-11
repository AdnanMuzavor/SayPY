"""Recursive approach"""


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)


"""Iterative approach"""


def factorial2(n):
    fact = 1
    for i in range(n):
        #print(i, "<", n)
        fact = fact*(i+1)
    return fact


print(factorial(4))
print(factorial2(5))

#series:    # 0 1 1 2 3 5 8 13
#positions: # 1 2 3 4 5 6 7 8


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(8))        
