import turtle
T = turtle.Pen()
T.penup()
turtle.bgcolor("black")
colors = ["Purple","Blue","Green","Yellow","Pink","Coral","Navy","Orange","Lime","Red"]

sides = int( turtle.numinput("Number Of Sides","Enter how many sides are there in your spiral of spiral(2 - 10)",4,2,10))
print(sides)
for x in range(100):
    T.forward(x*4)
    position = T.position()
    direction = T.heading()
    print(position,direction)
    for y in range(int(x/2)):
        T.pendown()
        T.pencolor(colors[y%sides])
        T.forward(2*y)
        T.right(360/sides-2)
        T.penup()
    T.setx(position[0])
    T.sety(position[1])
    T.setheading(direction)
    T.left(360/sides +2)
