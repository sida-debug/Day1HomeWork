import turtle
def drawPolygon(n):
    angle = 360/n
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(50)
        turtle.right(angle)
    turtle.end_fill()
    turtle.mainloop()
drawPolygon(10)