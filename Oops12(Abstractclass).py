from abc import ABC, abstractmethod

# This makes it a abstract class


class Shape(ABC):

    # This makes it abstarct method which means all the derived class, derived from shape muts have this method,else error will be thrown
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):
    def __init__(self):
        self.length = 10
        self.width = 20
    """Defining abstract method,if not defined and object of rectangle is cfeated it'll give an error"""

    def printarea(self):
        return self.length*self.width


r = Rectangle()
print(r.printarea())
