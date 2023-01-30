# import turtle package
import turtle

# shortening function names
t = turtle.Turtle()
sc = turtle.Screen()

# ask for window width and height from user
sc_width = int(input("Enter window width:\n"))
sc_height = int(input("Enter window height:\n"))

# set window width and height as defined by user
sc.setup(sc_width, sc_height)

# set background color
sc.bgcolor("blue")


turtle.mainloop()