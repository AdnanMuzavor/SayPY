l = 10  # global
print("l val before being chnaged using global var: ", l)


def function1(n):
    # local var, inaccesible outside fn
    v = 10
    # l=n
    """l=l+5 not possible as l is global variable"""

    """To change global variable follwing is done: """
    global l
    l = l+10
    print("In fn val: ", l, v)


# print(m) #error as undefined outside fn
function1(5)
print("Outside val fn(global var l is updated in fn using \"global keyword\"", l)


"""nesting of functions"""


def harry():
    x = 10

    def Rohan():
        global x
        x = 20
    print("X before calling fn: ", x)
    Rohan()
    print("X after calling fn: ", x)
    print("Value didn't changed as global keyword directly looks for var outside fn and not within fn in which curr fn is nested in")


harry()
print("X val is updated coz global keyword went directly out and made new global var with val 20,x: ", x)
