import turtle
from turtle import Turtle, Screen

screen = Screen
tim = Turtle("turtle")
tim.speed(-1)
def dragging(x,y):
    tim.ondrag(None)
    tim.setheading(tim.towards(x,y))
    tim.goto(x,y)
    tim.ondrag(dragging)

def clickright(x,y):
    tim.clear()

def main():
    turtle.listen()
    tim.ondrag(dragging)

    turtle.onscreenclick(clickright,3)

    turtle.mainloop()

main()