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


"""Long method of setting attributes"""

# Harry = Employee()  # Harry is object of class employee
# Rohan = Employee()  # Rohan is object of class employee

"""We acn assign different attriutes to this objects of class"""

# Harry.name = "Harry"
# Rohan.name = "Rohan"
# Harry.id = 12
# Rohan.id = 16

"""Short method of setting attributes using CONSTRUCTOR"""
Harry = Employee("Harry", 12)
print(Harry.printdetails())  # It's taken as prindetails(Harry)
Carry = Employee("Carry", 18)
print(Carry.printdetails())
