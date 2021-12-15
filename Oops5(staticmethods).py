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
    # enables obj of class to access class vars and change them
    @classmethod
    def changeempcount(cls, newcount):
        cls.empcount = newcount

    @classmethod
    def makeobjfromstr(cls, str):
        # returns list from string by splitting as per "-"
        params = str.split("-")
        print(params)
        # returns class employee with argumets as per constrctor definition
        return cls(*str.split("-"))  # i.e fn(*args) concept
        """Or"""
        return cls(params[0], params[1])

    @staticmethod
    def staticfn(str):
        print(f"I am static fn ,will print \"{str}\"")


"""Short method of setting attributes using CONSTRUCTOR"""
Harry = Employee("Harry", 12)
print(Harry.printdetails())  # It's taken as prindetails(Harry)
Carry = Employee("Carry", 18)
print(Carry.printdetails())

"""Using class methods to create obj in place of constructors"""
Karan = Employee.makeobjfromstr("Karan-20")
print(Karan.printdetails())

"""Calling static method"""
Harry.staticfn("Oh Static fn")
