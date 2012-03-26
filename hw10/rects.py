#!/usr/bin/env python
"""
rects.py

Pygame Rectangles
=========================================================
The following section will test your knowledge of how to 
use pygame Rect, arguably pygame's best feature. Define
the following functions and test to make sure they 
work with `python run_tests.py`

Make sure to use the documentation 
http://www.pygame.org/docs/ref/rect.html


Terms:
---------------------------------------------------------
  Point:     an x,y value
               ex:  pt = 3,4

  Polygon:   a shape defined by a list of points
               ex:  poly = [ (1,2), (4,8), (0,3) ]

  Rectangle:  pygame.Rect
"""

from pygame import Rect

# 1. poly_in_rect
#      Check to see if the polygon is completely within a given 
#      rectangle.
#
#      returns:  True or False


# In frist (commented out) version, a rect is created to be the boudns of the poly.  This method will trigger false positives if rect is inside the bounds, but not actually crossing with the polygon.
# In second version, simply check all points agaimnst rect, and hope that rect doesn't simply collide with a line or the center of the poly.
def poly_in_rect(poly, rect):
    '''xmax = xmin = ymax = ymin = 0
    for x, y in poly:
        if x > xmax:
            xmax = x
        elif x < xmin:
            xmin = x
        if y > ymax:
            ymax = y
        elif y < ymin:
            ymin = y
    '''
    #w = xmax-xmin
    #h = ymax-ymin
    #return rect.colliderect(Rect(xmin, ymin, w, h))
    
    flag = False
    for x, y in poly:
        if rect.collidepoint(x, y):
            flag = True
    
    return flag


# 2. surround_poly
#      Create a rectangle which contains the given polygon.  
#      It should return the smallest possible rectangle 
#      where poly_in_rect returns True.
#
#      returns:  pygame.Rect


# Reports an incorrect x, not sure why.
def surround_poly(poly):
    xmax = xmin = ymax = ymin = 0
    for x, y in poly:
        if x > xmax:
            xmax = x
        elif x < xmin:
            xmin = x
        if y > ymax:
            ymax = y
        elif y < ymin:
            ymin = y
    w = xmax-xmin
    h = ymax-ymin
    return Rect(xmin, ymin, w, h)
