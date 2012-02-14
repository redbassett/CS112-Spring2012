#!/usr/bin/env python

import pygame
from pygame.locals import *

## COLORS
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255

THICKNESS = 20


## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
pygame.display.set_caption("Olympic Rings   [press ESC to quit]")

## Draw
screen.fill(WHITE)

#################################
##  DRAW OLYPIC RINGS HERE
##
##  hint, lookup pygame.draw
##  specifically circle, ellipse,
##  and arc.  Also, the width
##  parameter
#################################
ringWidth = 25
shadowWidth = ringWidth + 10
ringRectSize = 250
shadowRectSize = ringRectSize + 10

pygame.draw.arc(screen, WHITE, Rect(15,0,shadowRectSize, shadowRectSize),0, 360, shadowWidth)
pygame.draw.arc(screen, BLUE, Rect(20,5,ringRectSize, ringRectSize), 0, 360, ringWidth)

pygame.draw.arc(screen, WHITE, Rect(145,130,shadowRectSize, shadowRectSize),0, 360, shadowWidth)
pygame.draw.arc(screen, YELLOW, Rect(150,135,ringRectSize, ringRectSize), 0, 360, ringWidth)

pygame.draw.arc(screen, WHITE, Rect(15,0,shadowRectSize, shadowRectSize),0, 90, shadowWidth)
pygame.draw.arc(screen, BLUE, Rect(20,5,ringRectSize, ringRectSize), 0, 360, ringWidth)

## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
