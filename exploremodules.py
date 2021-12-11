
import sys
import dis
from emoji import emojize
import turtle

"""Using turtle module"""
myTurtle = turtle.Turtle()
mywn = turtle.Screen()


def drawspirals(myTurtle, linelen):
    myTurtle.forward(linelen)
    myTurtle.right(190)
    drawspirals(myTurtle, linelen-10)


drawspirals(myTurtle, 800)
mywn.exitonclick()


"""Using emogis module"""

print(emojize(":thumbs_up:"))
print("woah thats grt,", emojize(":thumbs_up:"))


"""Disassembles a fn (dis) module"""


def test(number):
    return(str(number)+str(number))


def newfn():
    print("Hello")


dis.dis(test)
dis.dis(newfn)

"""sys module"""

while True:
    m = input("Type e to exit: ")
    if m == "e":
        sys.exit()
    print("you typed: ", m)
