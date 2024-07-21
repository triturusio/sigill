import importlib
import tomllib
import turtle
import pathlib
import time
import fig

SCREEN_WIDTH = 500
RESOLUTION = 50

def main():
    with open("settings.toml", "rb") as file:
        settings = tomllib.load(file)
        timestamp = 0
        screen = turtle.Screen()
        screen.setup(width=SCREEN_WIDTH, height=SCREEN_WIDTH)
        screen.title(settings["file"]["name"])
        render(screen, timestamp)
        turtle.done()

def render(screen, timestamp):
    new_timestamp = pathlib.Path('fig.py').stat().st_mtime
    if timestamp != new_timestamp: 
        importlib.reload(fig)
        turtle.reset()
        turtle.pensize(1)
        turtle.penup()
        turtle.goto(-RESOLUTION/2, -RESOLUTION/2)
        turtle.pendown()
        turtle.pencolor('red') 
        turtle.setheading(0)
        for _ in range(4): 
            turtle.forward(RESOLUTION) 
            turtle.right(-90) 
        fig.draw()
        time.sleep(1)
        screen.listen()
    screen.ontimer(lambda: render(screen, new_timestamp), 1000)

if __name__ == "__main__":
    main()