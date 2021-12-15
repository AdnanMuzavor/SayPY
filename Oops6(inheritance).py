# Abstraction->Hididng of implementation details
# Encapsulation->Grouping data and fns together
# Inheritance


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


"""Making class programmer which will hv all props of class employee"""


class Programmer(Employee):
    def __init__(self, name, id, lang, fname):
        super().__init__(name, id)  # class constructor of base class
        self.lang = lang
        self.fname = fname

    def printprog(self):
        return f"Name of Programmer is {self.name} and prog-id is: {self.id},languages known:{self.lang},other name: {self.fname}"
    pass


"""Making object using Programmer class"""
Prog1 = Programmer("Prog1", 18, ["pytho", "jav"], "progprog")
# Prog2 = Programmer.makeobjfromstr("Prog2-24")

print(Prog1.printdetails())  # Calling method of base class
print(Prog1.printprog())  # Calling method of derived class
