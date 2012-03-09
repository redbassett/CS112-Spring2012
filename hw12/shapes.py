import math

# Shapes
# =========================================================
# 
# Define a shape object.  This object has abstract (empty) 
# methods for calculating the area and perimeter of the 
# shape.
#
# After that, create classes for Rectangles, Squares, 
# and Circles.
# 
# When done, the code should work like this.
#     >>> r = Rect(3,4)
#     >>> print r.area()
#     12
#     >>> sq = Square(5)
#     >>> print sq.perimeter()
#     20
#     >>> print isinstance(sq, Rectangle)
#     True
#     >>> c = Circle(3)
#     >>> print c.area()
#     28.274333882308138
#     
class Shape(object):
    def __init__(self, *args):
        pass
    
    def perimeter(self):
        pass
    
    def area(self):
        pass

class Square(Shape):
    def __init__(self, *args):
        self.dim = args[0]
    
    def perimeter(self):
        return 4*self.dim
    
    def area(self):
        return self.dim**2

class Rect(Shape):
    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]
    
    def perimeter(self):
        return (2*self.x)+(2*self.y)
    
    def area(self):
        return self.x*self.y

class Circle(Shape):
    def __init__(Self, *args):
        self.r = args[0]
    
    def perimeter(self):
        



# Advanced Section
# ---------------------------------------------------------
# Add one more shape type: a polygon.  Polygons are created
# from a list of at least 3 points.
#
# >>> Polygon((0,0), (3,4), (0,4))
# >>> Polygon((0,0), (2,0), (2,2), (0,2))
#
# Perimeter should be easy to calculate, for area, use 
# method 1 on this site for finding the area of an irregular 
# polygon:
#   http://www.mathopenref.com/polygonirregulararea.html
# 
# You can find the area of a triangle with Heron's formula:
#   http://www.mathopenref.com/heronsformula.html
