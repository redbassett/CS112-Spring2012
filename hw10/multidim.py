#!/usr/bin/env python
"""
multidim.py

Multidimensional Arrays
=========================================================
This section checks to make sure you can create, use, 
search, and manipulate a multidimensional array.
"""


# 1.  find_coins
#       find every coin (the number 1) in a givven room
#          room: a NxN grid which contains coins

#          returns: a list of the location of coind
#
#       Example:
#       0 0 0 1 0 0
#       0 0 1 0 0 0
#       0 0 0 0 1 0
#       0 0 0 0 0 0
# 
#       >>> find_coins(room)
#       [ [3, 0], [2, 1], [4, 2] ]
#      


# Generates phantom coins.  Not sure how, can't read error messages
def find_coins(room):
    coins = []
    cury = 0
    for y in room:
        curx = 0
        for x in room[cury]:
            if room[cury][curx] == 1:
                coins.append([curx,cury])
            curx += 1
        cury += 1
    return coins


# 2. distance_from_player
#      calculate the distance from the player for each 
#      square in a room.  Returns a new grid of given
#      width and height where each square is the distance
#      from the player
import math

def distance(x1, y1, x2, y2):
    return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

# Once again, can't decode error.
def distance_from_player(player_x, player_y, width, height):
    grid = []
    y = 0
    while y < height:
        row = []
        x = 0
        while x < width:
            row.append(distance(player_x, player_y, x+1, y+1))
            x += 1
        grid.append(row)
        y += 1
    return grid
