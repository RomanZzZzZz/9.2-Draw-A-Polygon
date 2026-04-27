from turtle import *


sc = Screen()
sc.setup(600, 600)


tl = Turtle()
tl.speed(11)


def triangle():
    tl.forward(100)
    tl.left(120)
    tl.forward(100)
    tl.left(120)
    tl.forward(100)
    tl.left(120)


def pentagon():
    tl.forward(100)
    tl.left(72)
    tl.forward(100)
    tl.left(72)
    tl.forward(100)
    tl.left(72)
    tl.forward(100)
    tl.left(72)
    tl.forward(100)
    tl.left(72)


def hexagon():
    tl.forward(100)
    tl.left(60)
    tl.forward(100)
    tl.left(60)
    tl.forward(100)
    tl.left(60)
    tl.forward(100)
    tl.left(60)
    tl.forward(100)
    tl.left(60)
    tl.forward(100)
    tl.left(60)


def square():
    tl.forward(100)
    tl.left(90)
    tl.forward(100)
    tl.left(90)
    tl.forward(100)
    tl.left(90)
    tl.forward(100)
    tl.left(90)


def rectangle():
    tl.forward(150)
    tl.left(90)
    tl.forward(100)
    tl.left(90)
    tl.forward(150)
    tl.left(90)
    tl.forward(100)
    tl.left(90)


def parallelogram():
    tl.forward(150)
    tl.left(60)
    tl.forward(100)
    tl.left(120)
    tl.forward(150)
    tl.left(60)
    tl.forward(100)
    tl.left(120)


def trapezoid():
    tl.forward(150)
    tl.left(70)
    tl.forward(100)
    tl.left(110)
    tl.forward(100)
    tl.left(110)
    tl.forward(100)


sides = int(input("How many sides does your shape have? "))

if sides == 3:
    print("Triangle")
    triangle()

if sides == 4:
    print("Quadrilateral")
    equal_sides = input("Are all four sides equal yes or no: ")

    if equal_sides == "yes":
        print("Square")
        square()

    if equal_sides == "no":
        equal_angles = input("Are all four angles equal yes or no: ")

        if equal_angles == "yes":
            print("Rectangle")
            rectangle()

        if equal_angles == "no":
            parallel = input("How many pairs of parallel sides 1 or 2: ")

            if parallel == "2":
                print("Parallelogram")
                parallelogram()

            if parallel == "1":
                print("Trapezoid")
                trapezoid()

            if parallel != "1" and parallel != "2":
                print("Unknown quadrilateral")
                square()

if sides == 5:
    print("Pentagon")
    pentagon()

if sides == 6:
    print("Hexagon")
    hexagon()

if sides != 3 and sides != 4 and sides != 5 and sides != 6:
    print("Has to be 3, 4, 5, or 6 sides")


sc.exitonclick()