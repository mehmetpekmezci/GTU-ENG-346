import turtle as pen

def drawSide(length, depth):

    if depth == 0:
        pen.forward(length)
    else:
        new_length = length / 3.0
        drawSide(new_length, depth-1)
        pen.right(60)
        drawSide(new_length, depth-1)
        pen.left(120)
        drawSide(new_length, depth-1)
        pen.right(60)
        drawSide(new_length, depth-1)


# drawSide(100, 0)


def drawTriangle(sideLength, depth):
    drawSide(sideLength, depth)
    pen.left(120)
    drawSide(sideLength, depth)
    pen.left(120)
    drawSide(sideLength, depth)
    pen.left(120)

pen.pensize(5)

pen.pencolor('black')
drawTriangle(200, 0)
pen.pencolor('blue')
drawTriangle(200, 1)
pen.pencolor('red')
drawTriangle(200, 2)
pen.pencolor('green')
drawTriangle(200, 3)
# drawTriangle(200, 4)

pen.mainloop()
