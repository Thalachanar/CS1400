# project_2.py, test file for CS1400 Turtle Patterns I project
import turtle

t = turtle
t.tracer()



t.setup(500, 500)

def draw_rectangle(width, height, color):
    t.pendown()
    t.goto(width)
    t.goto(height)
    t.mainloop()

draw_rectangle()
