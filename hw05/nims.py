#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""


c = int(raw_input("Enter number of stones: "))
player = 1

while c > 0:
    move = 0
    while move == 0:
        move = int(raw_input("Player "+str(player)+", Enter a number: "))
    if move < c:
        c -= move
        if move > 1:
            s = 's'
        else:
            s = ''
        if c > 1:
            cs = 's'
        else:
            cs = ''
        print "Player "+str(player)+" removed "+str(move)+" stone"+s+", leaving "+str(c)+" stone"+cs+"."
        if player == 1:
            player = 2
        else:
            player = 1
    elif move == c:
        print "Player ",player," wins!"
        break
    else:
        print "That isn't a valid move!"
print "Game over."
