import turtle
T = turtle.Pen()
turtle.bgcolor("black")
T.pencolor("blue")
for x in range(24):
    T.penup()
    T.forward(x*4)
    T.pendown()
    T.write("Vihan")
    T.left(30)
    

