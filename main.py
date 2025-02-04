import importlib
import tomllib
from turtle import Turtle
import pathlib
import time
from context import Context
import fig

def main():
    with open("settings.toml", "rb") as file:
        settings = tomllib.load(file)
        file_name = settings["file"]["name"] 
        screen_size = settings["screen"]["size"]
        resolution = settings["file"]["resolution"]

        t = Turtle(visible=False)
        t.screen.setup(width=screen_size, height=screen_size)
        t.screen.title(file_name)

        render(t, context=Context(resolution=resolution), timestamp=0, resolution=resolution)

        t.screen.mainloop()


def render(turtle: Turtle, context, timestamp, resolution):
    new_timestamp = pathlib.Path('fig.py').stat().st_mtime
    try:
        if timestamp != new_timestamp: 
            importlib.reload(fig)
            turtle.reset()
            turtle.speed(0)
            turtle.hideturtle()
            turtle.pensize(1)
            turtle.penup()
            turtle.goto(-resolution/2, -resolution/2)
            turtle.pendown()
            turtle.pencolor('red') 
            turtle.setheading(0)
            for _ in range(4): 
                turtle.forward(resolution) 
                turtle.right(-90) 
            fig.draw(turtle, context=context)
            time.sleep(1)
            turtle.screen.listen()
    except:
        input("Press any key to retry.")
    finally:
        turtle.screen.ontimer(lambda: render(turtle, context, new_timestamp, resolution), 1000)


if __name__ == "__main__":
    main()