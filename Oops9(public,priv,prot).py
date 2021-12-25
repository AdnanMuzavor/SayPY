class Bird:
    fly = 10  # public
    _fly2 = 20  # protected
    __fly3 = 30  # private
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


# Public Private and protected are inherited
b = Bird()
b1 = EatingBird()
print(
    f"Accesing public member: {b1.fly}, accessing protected: {b1._fly2},Accesing private: {b1._Bird__fly3}")
