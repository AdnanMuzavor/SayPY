class Bird:
    fly = 10
    pass


class FlyingBird(Bird):
    #fly = 20

    def canfly(self):
        print("Bird can fly")
    pass


class EatingBird(FlyingBird):
    #fly = 30

    def canfly(self):
        print("Can fly and eat")
    pass


"""canfly fn in base class of class-3 is overwriytten by fn in class-3"""
b1 = EatingBird()
b1.canfly()
print(b1.fly)
"""If not in class-3,it'll search in class -2 and if not in class-2 thn serach in 1,else error if present in none"""
