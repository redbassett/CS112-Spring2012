#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

# def greeter(name):
def greeter(name):
    print "hello,",str(name).lower()

# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+

# def box(w,h):
def box(w,h):
    a = w
    b = h
    if w != '' and h != '':
        w = int(w)
        h = int(h)
    else:
        print "Error: Invalid Dimensions"
        return False

    if type(w) is str and type(h) is str and w > 0 and h > 0:
    #if w > 0 and h > 0:
        for x in range(h):
            printString = ''
            for y in range(w):
                if x == 0 or x == h-1:
                    if y == 0 or y == w-1:
                        printString += "+"
                    else:
                        printString += "-"
                else:
                    if y == 0 or y == w-1:
                        printString += "|"
                    else:
                        printString += " "
            print printString
    else:
        print "Error: Invalid Dimensions"

# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

# def tree()
def tree():
    return ""
