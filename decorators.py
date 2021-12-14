def fn1():
    print("Some fn")


fn2 = fn1
fn2()

"""Will fn2 be able to call fn1 if fn1 deleted,it will"""

del fn1
fn2()

"""We can return the functions"""


def fnreturner(num):
    if num == 0:
        return print
    if num == 1:
        return int
    if num == 2:
        return sum


a1 = fnreturner(0)  # hv builtin fn print
a2 = fnreturner(1)  # hv class int
a3 = fnreturner(2)  # hv builtin fn sum
print(a1, a2, a3)

"""We can execute a fn using other fn"""


def executor(fn):
    fn("Hello")


executor(print)


def executo2(fn, a, b):
    print(fn(a, b))


executo2(print, 2, 4)


def dec(fnc):
    def executor():
        print("Executing fn 1")
        fnc()
        print("Fn Executed")
    return executor


"""This keyword specifies that gn under @dec will be executed as executor fn inside dec fn, i.e statement above fnc1 ->fnc1 ->stateout below fnc1"""


@dec
def nameprinter():
    print("I am decorator based fn")


nameprinter()
