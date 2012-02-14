#!/usr/bin/env python
"""lists.py

A bunch of excercises to see if you understand list comprehensions
"""
import os

# Solve the following problems with one python statement.  It is fine 
# to break up the statement into multiple lines as long as it is only
# one actual command.
#
# This is fine:
#   print [ (x,y) 
#           for x in range(10)
#           for y in range(10) ]
#

# 1. Read a bunch of numbers from the input separated by spaces and 
#    convert them to ints
print "1.",  [int(_) for _ in raw_input("Enter a list of numbers: ").split()]

# 2.  Read another bunch of numbers, convert them, and return the list 
#     of only the first 3
print "2.", [int(_) for _ in raw_input("Enter a list of numbers: ").split()[:3]]

# 3.  Read a bunch of words separated by commas from the command line,
#     remove any excess spaces, and print a list of their lenghts
print "3.", [len(_) for _ in raw_input("Enter some words: ").split(',')]

# 4.  Create a list of every multiple of 3 between 1 and 100 with their 
#     index
#        ex:  [ [0,3], [1,6], [2,9]...]
print "4.", [[x,y] for x,y in enumerate(range(0, 100, 3))]

# 5. create a list of every card in a deck of cards 
print "5.", [str(card)+" of "+str(suit) for card in  range(1,14) for suit in ['Hearts', 'Clubs', 'Spades', 'Diamonds']]

# 6.  Create a 5 by 5 array filled with zeros
print "6.", [[y for y in range(0,5)] for x in range(0,5)]


# 7.  Make a list of every perfect square between 1 and 1000
print "7.", [_**2 for _ in range(0, 31)]

# 8.  Make a list of every perfect square between 1 and 1000 
#     a different way
#print "8.", []

# 9.  List every python file in this directory
print "9.", [_ for _ in os.listdir('./') if _.split('.')[1] == 'py']

# 10.  Print a list of every pythagorean triple with a side less than
#      or equal to 20.  Don't include duplicates ([3,4,5] == [4,3,5])
print "10.", [[a, b, c] for a in range(0, 20) for b in range(a, 20) for c in range(b, 20) if (a**2)+(b**2)==(c**2)]



############
#I DID NOT write this myself, adapted from examples of similar problems found.
############


# I couldn't in good concious include this, but it is fun to 
# figure out/find.

## NOT REQUIRED
# 11.  Print a list of every prime number less than 100
print "11.", [x for x in range(0, 100) if x not in [y for z in range(2, 8) for y in range(z*2, 100, z)]]
