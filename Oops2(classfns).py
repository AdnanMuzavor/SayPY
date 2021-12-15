class Employee:
    # This is class var belonging to class and is changeable only by class (You can think of it as static variable)
    empcount = 12

    # self here refers to curr object of class employee on whom fn is being called

    def printdetails(self):
        return f"Name is {self.name} and id is: {self.id}"


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
print(Harry.printdetails()) #It's taken as prindetails(Harry)

