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

# This is actually wrong as we are'nt suppose to tell user info
# hence attribute email is removed
# print(Harry.email)

"""When email is defined just as a function"""
""" -> Harry.email()"""

"""After making email a property"""
"""This will print the email"""
print(Harry.email)

# Email is dynamically defined property, what if we reset it
# Hence i n that case our fname and lname should also change

"""Without having a setter"""
# Harry.email="Carry.Parry@gmail.com"
# Harry.printdetails()
"""This will give error saying "Can't set attribute email" """

"""Defining a setter"""
Harry.email = "Carry.Parry@gmail.com"
Harry.printdetails()
"""This will not give an error saying "Can't set attribute email" as email.setter is now defined for property email """

"""Without having a deleter"""
#del Harry.email
# Harry.printdetails()
"""This will give error saying "Can't delete attribute email" """

"""Defining a deleter"""
del Harry.email
Harry.printdetails()
"""This will not give an error saying "Can't delete attribute email" as email.deleter is now defined for property email """

Harry.email = "Harry.Rohan@gmail.com"
Harry.printdetails()
