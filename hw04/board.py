#!/usr/bin/env/ python

w = int(raw_input("Width: "))
h = int(raw_input("Height: "))
toggle = False
for y in range(0,h):
    line = ''
    for x in range(0,w):
        if toggle:
            line += '-'
            toggle = False
        else:
            line += '#'
            toggle = True
    print line
