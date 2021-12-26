import inspect


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        #self.email = fname+"."+lname+"@remail.com"
        # self.email=f"{self.fname}.{self.lname}@gmail.com"
        pass

    def printdetails(self):
        if self.fname == None or self.lname == None:
            print("Vales not set")
            return
        print(f"Fname: {self.fname}, Lname: {self.lname}, Email: {self.email}")

    """Defining email as property"""
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"

    """Defining a setter for property email"""
    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    """Defining deleter for property email"""
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


Harry = Employee("Harry", "Parry")
Harry.printdetails()
Harry.email = "Harry.Rohan@gmail.com"
Harry.printdetails()
print(Harry)
"""Prints type"""
print(type(Harry))
print(type("hello"))

"""Prints id"""
print(id(Harry))
print(id("hello-2"))

"""Print entire directory/attributes"""
print(dir(Harry))
print(dir("hello-3"))

print(inspect.getmembers(Harry))

"""Printing ech attribute systametically"""
objlist = f"{dir(Harry)}".split(",")
i = 0
for item in objlist:
    print(f"Item-no-{i} -> {item}")
    i += 1
