import math
import points

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

class Rect(Shape):
    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]
    
    def perimeter(self):
        return (2*self.x)+(2*self.y)
    
    def area(self):
        return self.x*self.y

class Square(Rect):
    def __init__(self, *args):
        self.x = self.y = args[0]


class Circle(Shape):
    def __init__(self, *args):
        self.r = args[0]
    
    def perimeter(self):
        return math.pi*2*self.r
    
    def area(self):
        return (self.r**2)*math.pi


class Polygon(Shape):
    def __init(self, *args):
        for arg in args:
            self.points.append(arg)
        self.pts = self.points # Attempt to please the stupid tester that doesn't actual explain the error.
    
    def perimeter(self):
        # For lack of algorithm, hope points are listed in order around shape.
        prev = None
        per = 0
        
        for point in self.points:
            tmp = Point(point)
            if prev is None:
                prev = Point(self.point[len(self.points)-1])
            per += tmp.distance(prev)
            prev = tmp
        
        return per

    def area(self):
        area = 0
        j = len(self.points)-1
        i = 0
        
        for point in self.points:
            area += (self.points[j][0]+point[0])*(self.points[j][1]-point[1])
            i += 1
            j = i
        
        return area/2


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
