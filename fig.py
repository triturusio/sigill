from turtle import Turtle
from sigill import Context

def draw(turtle: Turtle, context: Context):
    drawable = context.resolution*context.scale*0.70
    origin = (-drawable/2, -drawable/2)
    circle_count = 10

    radius = drawable/circle_count
    stroke = 3*context.scale

    turtle.width(stroke)
    turtle.penup()
    turtle.goto(x=origin[0], y=origin[1])

    if context.show_guides:
        turtle.pendown()
        turtle.pencolor('gray') 
        turtle.setheading(0)
        for _ in range(4): 
            turtle.forward(drawable) 
            turtle.right(-90) 

    turtle.pencolor('black') 

    for y in range(-1, circle_count):
        for x in range(0, circle_count+1):
            turtle.penup()
            turtle.goto(x=origin[0]+radius*x, y=origin[1]+radius*y)
            turtle.pendown()
            turtle.circle(radius, steps=100)