import turtle
import random

tim = turtle.Turtle()
colors = ['red','blue','green','purple','yellow','orange','black']

#set coloer for turtle
tim.color('red','blue')
tim.width(5)

#Fill in shape with color
tim.begin_fill()
tim.circle(50)
tim.end_fill()

#prepare to draw a square

tim.penup()
tim.forward(200)
tim.pendown()

tim.color('green','black')

tim.begin_fill()
for turtle_motion in range(4):
    tim.forward(100)
    tim.right(90)
tim.end_fill()

#random circles in the screen

for x in range(20):
    randColor = random.randrange(0,len(colors))
    tim.color(colors[randColor])
    rand1 = random.randrange(-300,300)
    rand2 = random.randrange(-300,300)
    tim.penup()
    tim.setpos((rand1,rand2))
    tim.pendown()
    tim.begin_fill()
    tim.circle(random.randrange(0,80))
    tim.end_fill()