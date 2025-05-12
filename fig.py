from turtle import Turtle
from sigill import Context

def draw(turtle: Turtle, context: Context):
    drawable = context.resolution*context.scale*0.70
    radius = 2*context.scale
    stroke = 20*context.scale


    turtle.width(stroke)
    turtle.pencolor('black') 
    turtle.penup()
    turtle.goto(-drawable/2, -drawable/2)

    turtle.pendown()
    turtle.forward(10)