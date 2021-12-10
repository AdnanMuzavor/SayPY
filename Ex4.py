n = int(input("Enter number n: "))
boolean = int(input("Enter 1 or 0: "))

if boolean == 1:
    boolval = True
else:
    boolval = False

print(boolean)

if boolval:
    i = 0
    j = 0
    while i < n:
        j = 0
        while j <= i:
            print(" * ", end="")
            j += 1
        print("\n")
        i += 1
else:
    i = n
    j = n
    while i != 0:

        j = i
        while j != 0:
            print(" * ", end="")
            j -= 1
        print("\n")
        i -= 1
