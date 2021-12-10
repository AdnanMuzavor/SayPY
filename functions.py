a=10
b=14

#built in functions
c=sum((a,b))
print(c)

#user defined functions
def function1(a,b):
    """This is docstring: first line in function"""
    print("Inside fn",a+b)
    print("average: ",(a+b)/2)
    return (a+b)/2

v=function1(2,6)
print(v)
print(function1.__doc__)