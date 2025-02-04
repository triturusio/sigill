from turtle import Turtle
from context import Context

def draw(turtle: Turtle, context: Context):
    drawable = context.resolution*0.75

    iteration = 4
    radius = 5
    length = drawable / (2**iteration - 1)
    size = length - radius

    turtle.width(5)
    turtle.pencolor('black') 
    turtle.penup()
    turtle.goto(-drawable/2, -drawable/2)
    turtle.forward(radius)
    turtle.pendown()

    operations = []

    hilbert(iteration=iteration, length=size, angle=90, radius=radius, operations=operations)

    skip = False
    forward = 0

    for index in range(0, len(operations)):
        if skip:
            skip = False
            continue
        if -operations[index][1] == operations[index+1][1] :
            skip = True
            continue
        if operations[index][0] > 0:
            if forward > 0:
                turtle.forward(operations[index][0]+radius)
            else:
                turtle.forward(operations[index][0]-radius)
            forward += 1
        else:
            turtle.circle(operations[index][1], operations[index][2])
            forward = 0


def hilbert(iteration, length, angle, radius, operations):
    if (iteration == 0):
        return
    else:
        operations.append((0, radius, angle))
        hilbert(iteration - 1, length, angle, -radius, operations)
        operations.append((length, 0, 0))
        operations.append((0, -radius, angle))
        hilbert(iteration - 1, length, angle, radius, operations)
        operations.append((length, 0, 0))
        hilbert(iteration - 1, length, angle, radius, operations)
        operations.append((0, -radius, angle))
        operations.append((length, 0, 0))
        hilbert(iteration - 1, length, angle, -radius, operations)
        operations.append((0, radius, angle))