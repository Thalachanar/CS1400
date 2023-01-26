# project_2.py, test file for CS1400 Turtle Patterns I project
import turtle
import math

if __name__ == "__main__":
    t = turtle.Turtle()

    def drawRectangle(width, height, tilt, penColor, fillColor):
        """
        draw a rectangle with a given width, height, penColor and fillColor,
        with the current location of the turtle being the 
        lower left corner, and the bottom side tilted by an angle tilt (specified in degrees)
        relative to the horizontal axis. Use a turtle called t to create the drawing
        """

        # Insert code to draw the rectangle
        
    def drawTriangle(base, height, tilt, penColor, fillColor):
        """
        draw a triangle with a given base, height, penColor and fillColor,
        with the current location of the turtle being the 
        lower left corner, and the bottom side tilted by an angle tilt (specified in degrees)
        relative to the horizontal axis. Use a turtle called t to create the drawing
        """

        # Insert code to draw the rectangle
    
    def drawTree(height, color):
        
        ''' 
        This function draws a tree with a specific height and color, with the bottom of the bark at the current location of the turtle. The bark of the tree is always brown. All other parameters such as the width of the tree and the length of the bark are chosen so that the tree is well proportioned. The tree top is composed of three triangles stacked on top of each other.
        '''
    def testdrawTree():
        
        t.up()
        t.goto(0,-400)
        t.down()
        drawRectangle(200, 200, 0, "red", "")
        drawTree(200, "green")

    testdrawTree()
