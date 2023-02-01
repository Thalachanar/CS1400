'''
Project Name: Turtle Patterns I
Author: Dawson Allen
Due Date: 2023-02-03
Course: CS1400-001

Draw two rectangles.    A full project would need more code.
'''
import turtle

t = turtle.Turtle()
# (3) add functions here that your main program calls
# to do stuff.
def draw_rect(width, height, penc, fillc, penw):
    '''
    Draw a rectange given the width, height, pen-color (penc),
    fill-color (fillc), and pen-width (penw).

    NOTE: This is not yet fully implemented, and your solution could
      contain additional parameters!
    '''
    turtle.pd()
    turtle.begin_fill()
    for _i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.pu()

def get_dimensions():
    # (1) replace pass with your code
    width = int(input('Window width: '))
    height = int(input('Window height: '))
    if width <= 0 or height <= 0:
        print('Width and height must be positive integers')
        raise ValueError('Width and height must be positive integers')

    return (width, height)

def draw(width, height):
    '''
    Sets the size of the screen to width and height and draws a doodle.
    '''
    # (2) replace pass with your code
    turtle.setup(width, height)

    turtle.pu()
    turtle.goto(-200, 100)
    draw_rect(120, 80, 'black', 'yellow', 4)

    turtle.pu()
    turtle.goto(200, 100)
    draw_rect(120, 80, 'black', 'yellow', 4)