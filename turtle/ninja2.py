import turtle
ninja = turtle.Turtle()
ninja.speed(10)
for i in range(100):
    ninja.forward(40)
    ninja.right(5)
    ninja.left(10)
    ninja.forward(50)
    ninja.left(20)
    ninja.forward(60)
    ninja.right(10)
    ninja.penup()
    ninja.setposition(0,0)
    ninja.pendown()
    ninja.right(4)
turtle.done    