import os
import argparse
import importlib
import tomllib
from turtle import Turtle
from PIL import Image
import pathlib
import time
from context import Context
import fig

def main():
    try: 
        with open("settings.toml", "rb") as file:
            settings = tomllib.load(file)
            file_name = settings["file"]["name"] 
            screen_size = settings["screen"]["size"]
            resolution = settings["file"]["resolution"]
            context = Context(resolution=resolution, name=file_name)

            parser = argparse.ArgumentParser( 
                prog='Sigill', 
                description='Render Options',
                epilog='Found any issues? Please submit a bug report at [...]'
            )
            parser.add_argument('--export', action=argparse.BooleanOptionalAction)
            args = parser.parse_args()

            t = Turtle(visible=False)
            t.screen.setup(width=screen_size, height=screen_size)
            t.screen.title(file_name)

            if (args.export):
                export(t, context)
            else:
                render(t, context, timestamp=0)

            t.screen.mainloop()
    except Exception as e: 
        print("Error: ", e)
    
def export(turtle: Turtle, context: Context):
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(1)
    turtle.penup()
    turtle.goto(-context.resolution/2, -context.resolution/2)
    turtle.pendown()
    turtle.setheading(0)

    fig.draw(turtle, context)

    os.makedirs("./out", exist_ok = True)
    file_name = f"./out/{context.name}_{context.resolution}x{context.resolution}"

    turtle.screen.getcanvas().postscript(
        file = f"{file_name}.ps", 
        x = -context.resolution/2, 
        y = -context.resolution/2, 
        height = context.resolution+1, 
        width = context.resolution+1, 
        colormode = 'color'
    )

    psimage = Image.open(f"{file_name}.ps")
    psimage.save(f"{file_name}.png")

    print("export complete")


def render(turtle: Turtle, context: Context, timestamp):
    new_timestamp = pathlib.Path('fig.py').stat().st_mtime
    try:
        if timestamp != new_timestamp: 
            importlib.reload(fig)
            turtle.reset()
            turtle.speed(0)
            turtle.hideturtle()
            turtle.pensize(1)
            turtle.penup()
            turtle.goto(-context.resolution/2, -context.resolution/2)
            turtle.pendown()
            turtle.pencolor('red') 
            turtle.setheading(0)
            for _ in range(4): 
                turtle.forward(context.resolution) 
                turtle.right(-90) 
            fig.draw(turtle, context)
            time.sleep(1)
            turtle.screen.listen()
    except Exception as e: 
        print("Error: ", e)
        input("Press any key to retry.")
    finally:
        turtle.screen.ontimer(lambda: render(turtle, context, new_timestamp), 1000)

if __name__ == "__main__":
    main()