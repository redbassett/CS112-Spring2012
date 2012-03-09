import math
# Point Object
# =====================================
# Create a Point point class.  Point objects, when created, look like this:
#     >>> pt = Point(3,4)
#     >>> print pt.x
#     3
#     >>> print pt.y
#     4
#
# In addition points have the following methods:
#    distance(self, other):
#        calculates the distance between this point and another
#    
#    move(self, x, y):
#        sets the points location to x,y
# 
#    translate(self, x, y):
#        offsets the point by x and y
# 
#    When all done, points should work like this:
#
#    >>> a = Point(0,0)
#    >>> b = Point(0,0)
#    >>> b.move(2, 2)
#    >>> print b.x, b.y
#    2 2
#    >>> b.translate(1,2)
#    >>> print b.x, b.y
#    3 4
#    >>> print a.distance(b)
#    5
#
class Point(object):
    def __init__(self, x, y):
        self.move(x, y)
    
    def translate(self, x, y):
        self.x += x
        self.y += y
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        return math.sqrt(((other.x-self.x)**2+(other.y-self.y)**2))
    
    def slope(self, other):
        return (other.y-self.y)/(other.x-self.x)
    
    def extrapolate(self, slope, distance):
        pass
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'






# Advanced Section:
# ---------------------------------------
# Add the following function:
#     slope(self, other):
#         calculate the slope between two points
#
#     extrapolate(self, slope, distance):
#         returns a point along the line defined by slope
#         a given distance away
#
# Also, add the following special python methods:
#     __eq__(self, other):
#         checks if other is a Point and is equal to self
#
#     __str__(self):
#         returns a string representation of the point 
#     
#     >>> print Point(3,4)
#     (3,4)
#     >>> a = Point(1,2)
#     >>> b = Point(1,2)
#     >>> print a == b
#     True
