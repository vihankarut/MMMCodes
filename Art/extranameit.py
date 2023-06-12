import turtle
T = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","purple","light blue","pink","white"]
sides = int(turtle.numinput("Number Of Sides","How many sides do you want? 1 - 8 ",4,1,8))
for x in range(360):
    T.pencolor(colors[x%sides])
    T.forward(x*3/sides+x)
    T.left(120/sides+1)                                                                           
    T.width(x*sides/200)
    
