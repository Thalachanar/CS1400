'''
Project Name: Turtle Patterns I
Author: Dawson Allen
Due Date: 2023-02-03
Course: CS1400-001

Draw two rectangles.    A full project would need more code.
'''
import turtle

t = turtle.Turtle()

def draw_circ(radius, x_coor, y_coor, fillc):
    t.pu()
    t.goto(x_coor, y_coor)
    t.pd()
    t.begin_fill(fillc)
    t.circle(radius)
    t.end_fill()
    t.pu()
    
def get_dimensions():
    width = int(input('Window width: '))
    height = int(input('Window height: '))
    if width <= 0 or height <= 0:
        print('Width and height must be positive integers.')
        raise ValueError('Width and height must be positive integers.')
    return (width, height)

def draw(width, height):
    turtle.setup(width, height)
    
    draw_circ(400, 0, -200, "yellow")


turtle.mainloop()