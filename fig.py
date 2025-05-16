from turtle import Turtle
from sigill import Context

# Change this method to draw your icon
def draw(turtle: Turtle, context: Context):
    safe_area_side_length = context.resolution*context.scale*0.75

    # Using guides to draw the safe area of the icon. These guide are not included in the export.
    if context.show_guides:
        turtle.penup()
        turtle.goto(x=-safe_area_side_length/2, y=-safe_area_side_length/2)
        turtle.pendown()
        turtle.pencolor('gray') 
        turtle.width(1) 
        turtle.setheading(0)
        for _ in range(4): 
            turtle.forward(safe_area_side_length) 
            turtle.right(-90) 
        turtle.penup()

    # Adjustable parameters for the icon.
    inner_stroke = 10*context.scale
    outer_stroke = 20*context.scale
    length = safe_area_side_length/2
    count = 10 
    turtle.pencolor('black') 

    # Draws outline.
    turtle.width(outer_stroke)

    turtle.penup()
    turtle.goto(x=0, y=0)
    turtle.setheading(180)
    turtle.forward(length)
    turtle.setheading(60)
    turtle.pendown()
    turtle.forward(length)

    turtle.setheading(0)
    turtle.forward(length)

    turtle.setheading(-60)
    turtle.forward(length)

    turtle.setheading(-120)
    turtle.forward(length)

    turtle.setheading(180)
    turtle.forward(length)

    turtle.setheading(120)
    turtle.forward(length)

    # Draws inner lines.
    turtle.width(inner_stroke)

    for offset in range(0, count):
        turtle.penup()
        turtle.goto(x=0-length/count*offset, y=0)
        turtle.setheading(60)
        turtle.pendown()
        turtle.forward(length)

    for offset in range(0, count):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(-60)
        turtle.forward(length/count*offset)
        turtle.setheading(180)
        turtle.pendown()
        turtle.forward(length)

    for offset in range(0, count):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(60)
        turtle.forward(length/count*offset)
        turtle.setheading(-60)
        turtle.pendown()
        turtle.forward(length)
