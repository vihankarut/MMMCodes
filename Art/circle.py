import turtle
turtle.bgcolor("black")
T = turtle.Pen()
T.pencolor("white")
circles = int(turtle.numinput("Number of Circles","How many sides do you want",4))
T.width(110)
for x in range(circles):
    T.circle(100)
    T.left(360/circles)
T.pencolor("Yellow")
for x in range(circles):
    T.circle(50)
    T.left(360/circles)
