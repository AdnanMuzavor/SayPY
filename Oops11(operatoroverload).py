from typing import Counter


class Employee:
    # This is class var belonging to class and is changeable only by class (You can think of it as static variable)
    empcount = 12
    # Making a constructor

    def __init__(self, name, id):
        self.name = name
        self.id = id
        pass

    # self here refers to curr object of class employee on whom fn is being called

    def printdetails(self):
        return f"Name is {self.name} and id is: {self.id}"

    def printdetails2(self):
        return f"Name is {self.name} and id is: {self.id} str!!"

    """Overloading add operator"""

    def __add__(self, other):
        return self.id+other.id

    """Overloading add operator"""

    def __truediv__(self, other):
        return self.id/other.id

    """Overloading repr, used when defining/printing object"""

    def __repr__(self):
        return self.printdetails()
        pass

    def __str__(self):
        return self.printdetails2()
        pass


"""Short method of setting attributes using CONSTRUCTOR"""
Harry = Employee("Harry", 12)
print(Harry.printdetails())  # It's taken as prindetails(Harry)
Carry = Employee("Carry", 18)
print(Carry.printdetails())

# With help of operator overloading,this will print addition of ids
print(Harry+Carry)
# With help of operator overloading,this will print division of ids
print(Harry/Carry)
# While printing object it uses repr by default if defined,else uses str by default if defined
print(Harry)
