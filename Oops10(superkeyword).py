"""super key word is used to call constructor of base class as it might hv some necesaary initialisation """
#syntax: super().__init__()


class A:
    classvar1 = "I am class var of class -A"

    def __init__(self):
        self.var1 = "I am class - A constrcutor var1 "
        pass


class B(A):
    var1 = "I am class - B constructor var1"
    classvar2 = "I am base class - B's var2"


b = B()
print(b.var1)

# Case study->
"""Although there is var1 in class B it prints var1 of base class coz constructor of base class ran as soon as object was made"""

# class C:
#     classvar1="I am class var of class -A"
#     def __init__(self):
#         self.var1="I am class - A constrcutor var1 "
#         pass

# class D(C):
#     def __init__(self):
#         self.var2="I am var-2 defined in constructor of base class"
#     classvar2="I am base class - B's var2"

# b2=D()
# print(b2.var1)

# Case study->
"""Constrcutor of base class is overwritten by constructor of derived class hence it won't be able to foind var-1 and give error"""


class A1:
    classvar1 = "I am class var of class -A"

    def __init__(self):
        self.var1 = "I am class - A constrcutor var1 "
        pass


class B1(A1):
    def __init__(self):
        self.var1 = "I am class - B constructor var1"
        self.classvar2 = "I am base class - B's var2"
        super().__init__()


b2 = B1()
print(b.var1)

# Case study->
"""Constructor of derived class is called first which already as var1 named variable but thn base class also has var1 which overwrites var1 of derived"""


class A2:
    classvar1 = "I am class var of class -A"

    def __init__(self):
        self.var1 = "I am class - A constrcutor var1 "
        pass


class B2(A2):
    def __init__(self):
        super().__init__()
        self.var1 = "I am class - B constructor var1"
        self.classvar2 = "I am base class - B's var2"


b3 = B2()
print(b3.var1)

# Case study->
"""Constructor of base class is called first which already as var1 named variable but thn derived class also has var1 is overwrites var1 of base"""
