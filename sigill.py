import os
import argparse
import importlib
import string
import tomllib
import pathlib
import time
import fig
from turtle import Turtle
from PIL import Image

class Context:
    resolution: int = 0
    """Figure resolution"""

    scale: float = 0
    """Scale of any pixel value"""

    name: string  = ""
    """Figure name"""

    show_guides: bool = False
    """Guide not visible when exported"""

    def __init__(self, resolution: int, name: string, scale: float, show_guides: bool):
        self.resolution = resolution
        self.name = name
        self.scale = scale
        self.show_guides = show_guides

def main():
    try: 
        parser = argparse.ArgumentParser( 
            prog='Sigill', 
            description='Render Options',
            epilog='Found any issues? Please submit a bug report at [...]'
        )
        parser.add_argument('--export', action=argparse.BooleanOptionalAction)
        args = parser.parse_args()

        with open("settings.toml", "rb") as file:
            settings = tomllib.load(file)
            file_name = settings["file"]["name"] 
            screen_size = settings["screen"]["size"]

            t = Turtle(visible=False)
            t.screen.setup(width=screen_size, height=screen_size)
            t.screen.title(file_name)

            resolution = settings["file"]["resolution"]
            
            if (args.export):
                scales = settings["file"]["scales"]
                for scale in scales:
                    export(
                        turtle=t, 
                        context=Context(
                            resolution=resolution, 
                            name=file_name, 
                            scale=scale,
                            show_guides=False
                        )
                    )
                    print(f"{scale}X complete")
            else:
                scale = settings["screen"]["scale"]
                render(
                    turtle=t, 
                    context=Context(
                        resolution=resolution, 
                        name=file_name, 
                        scale=scale,
                        show_guides=True
                    ), 
                    timestamp=0)
                t.screen.mainloop()

    except Exception as e: 
        print("Error: ", e)
    
def export(turtle: Turtle, context: Context):
    turtle.reset()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(1)
    turtle.penup()
    turtle.goto(-context.scale*context.resolution/2, -context.scale*context.resolution/2)
    turtle.pendown()
    turtle.setheading(0)

    fig.draw(turtle, context)
    os.makedirs("out", exist_ok = True)

    file_name = f"out/{context.name}_{context.scale}X"

    turtle.screen.getcanvas().postscript(
        file = f"{file_name}.ps", 
        x = -context.scale*context.resolution/2, 
        y = -context.scale*context.resolution/2, 
        height = context.scale*context.resolution+1, 
        width = context.scale*context.resolution+1, 
        colormode = 'color'
    )

    psimage = Image.open(f"{file_name}.ps")
    psimage.save(f"{file_name}.png")

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
            turtle.goto(-context.resolution*context.scale/2, -context.resolution*context.scale/2)
            turtle.pendown()
            turtle.pencolor('red') 
            turtle.setheading(0)
            for _ in range(4): 
                turtle.forward(context.resolution*context.scale) 
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