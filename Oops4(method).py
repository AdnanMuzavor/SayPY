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

    # class method->Method to change/access class vars
    #enables obj of class to access class vars and change them
    @classmethod
    def changeempcount(cls, newcount):
        cls.empcount = newcount


"""Short method of setting attributes using CONSTRUCTOR"""
Harry = Employee("Harry", 12)
print(Harry.printdetails())  # It's taken as prindetails(Harry)
Carry = Employee("Carry", 18)
print(Carry.printdetails())

Harry.empcount = 18  # won't work on class var but..
print(Employee.empcount)
# Change class var empcount since changeempcount is class method
Harry.changeempcount(18)
print(Harry.empcount)
