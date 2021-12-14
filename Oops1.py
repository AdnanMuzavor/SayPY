class Employee:
    # This is class var belonging to class and is changeable only by class (You can think of it as static variable)
    empcount = 12
    pass


"""To get to know all attributes a aclass has"""
print(Employee.__dict__)

Harry = Employee()  # Harry is object of class employee
Rohan = Employee()  # Rohan is object of class employee

"""We acn assign different attriutes to this objects of class"""
print(Harry.__dict__, Rohan.__dict__)  # Initially won't hv anything
Harry.name = "Harry"
Rohan.name = "Rohan"
Harry.id = 12
Rohan.id = 16
# You'll be able to see assigned attributes
print(Harry.__dict__, Rohan.__dict__)

"""Accessing assihgned attributes"""
print(Harry.name, Rohan.name)

"""Accesing class variable i.e empcount"""
print(Harry.empcount)

"""An object cannot change class variable"""
"""This is bcom Harry.empcount will make variable for harry object without affecting class variable"""
print(Harry.__dict__, Rohan.__dict__) #empcount attribute not there for object harry
Harry.empcount = 18
print(Harry.__dict__, Rohan.__dict__) #empcount attribute there for objectb harry
print(Harry.empcount)

"""Class can change it's own variable"""
print(Employee.empcount)  # accesing var with class name
Employee.empcount = 20
print(Harry.empcount)  # Accessing with object name
