import turtle
T = turtle.Pen()
turtle.bgcolor("black")
colors = ["Purple","Blue","Green","Red","Pink","Coral","Navy","Orange","Lime","Yellow"]
family = []
name = turtle.textinput("family","Enter a name ")
while name !="":
    family.append(name)
    name = turtle.textinput("family","Enter a name or hit enter to exit")
for x in range(100):
    T.pencolor(colors[x%len(family)])
    T.penup()
    T.forward(x*4)
    T.pendown()
    T.write(family[x%len(family)],font = ("Arial",int((x+4)/4),"bold"))
    T.left(360/len(family)+2)
