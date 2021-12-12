"""Method-1"""

me = "Harry"
al = 3
a = "This is %s, roll no: %d" % (me, al)
print(a)

"""Method-2"""
me2 = "Rohan"
al2 = 4
a2 = "This is {}, roll no: {}"
b2 = a2.format(me2, al2)  # 0,1
print(b2)

me3 = "Rohani"
al3 = 40
a3 = "This is {1}, roll no: {0}"  # placing val at 1 first thn val at 0
b3 = a3.format(me3, al3)  # 0,1
print(b3)

"""But this is tideous task so we use FSTRINGS"""
"""You can directly place var names at place you want"""
a4 = f"this is roll no of {me}  and has val: {al},code is: {4*65}"  # FSTRING , f full form is fast
print(a4)
