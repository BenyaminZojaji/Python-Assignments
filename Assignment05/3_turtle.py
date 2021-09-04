import turtle
turtle.title("Benyamin\'s Turtle ^^")
t = turtle.Pen()
t.shape("turtle")
t.speed(2.5)
turtle.bgcolor('white')
t.penup()
t.pendown()
i, j= 0, 0
side=0
while i < 10:
    t.left(180-((((i+3-2)*180)/(i+3))/2))
    side=106+side
    while j <= i+2:
        t.pencolor('black')
        t.width(1.5)
        t.forward(side/(i+3))
        t.left(180-(((i+3-2)*180)/(i+3)))
        j += 1
    t.penup()
    t.right(180-(((i+3-2)*180)/(i+3)))
    t.right((((i+3-2)*180)/(i+3))/2)
    t.forward(17)
    t.pendown()
    j=0
    i+=1
