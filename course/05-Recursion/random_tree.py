import turtle as pen
import random

def treeRandom(length, minLength, thickness, minThickness, minAngle, maxAngle, minShrink, maxShrink):

    if (length < minLength) or (thickness < minThickness): # Base case
       pass # Do nothing
    else:
        angle1 = random.uniform(minAngle, maxAngle)
        angle2 = random.uniform(minAngle, maxAngle)
        shrink1 = random.uniform(minShrink, maxShrink)
        shrink2 = random.uniform(minShrink, maxShrink)
        pen.pensize(thickness)
        pen.forward(length)
        pen.right(angle1)
        treeRandom(length*shrink1, minLength, thickness*shrink1,minThickness, minAngle, maxAngle, minShrink, maxShrink)
        pen.left(angle1 + angle2)
        treeRandom(length*shrink2, minLength, thickness*shrink2,minThickness, minAngle, maxAngle, minShrink, maxShrink)
        pen.right(angle2)
        pen.pensize(thickness)
        pen.backward(length) 


def initialize_pen():
    pen.up()
    pen.left(90)
    pen.goto(0, -100)
    pen.down()

initialize_pen()

random.seed(100)

treeRandom(100, 5, 10, 1, 10, 45, 0.6, 0.9)
# treeRandom(100, 60, 10, 1, 10, 45, 0.1, 0.9)

pen.mainloop()
