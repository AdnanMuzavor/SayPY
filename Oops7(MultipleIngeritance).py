# Abstraction->Hididng of implementation details
# Encapsulation->Grouping data and fns together
# Inheritance
"""Multiple inheritance"""

# derived-class(base1,base2)
# ->Constructor of base1 will be called
# ->Fns(same name as in base2) from base1 will be called


class Employee:
    #var1=24
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


"""Making class player"""


class Player:
    var1=20
    def __init__(self, score, game):
        self.score = score
        self.game = game
        pass

    def printdetails(self):
        print(f"player played {self.game} and got score {self.score}")

"""Making class coolemployee who will be employee as well as player"""
class CoolEmployee1(Employee,Player):
   # var1=18
   pass
  

"""Making class coolemployee who will be employee as well as player"""
class CoolEmployee2(Player,Employee):
    var1=12
   

"""Since employee class is written first,It'll call constuctor of employee class, if I try to give argument as per constructor of player class,it'' give aqn error,Also printdetails method of Employe class is executed"""

Harry=CoolEmployee1("Harry",12)
print(Harry.printdetails())
print(Harry.var1)
"""Trying to access var, if present in serived class will get displayed else eill be searhed in base class-1 and thn base class-2"""




"""Since player class is written first,It'll call constuctor of player class, if I try to give argument as per constructor of employee class,it'' give aqn error,Also printdetails method of player class is executed"""

Rohan=CoolEmployee2(12,"vkjc q")
print(Rohan.printdetails())


