#!/usr/bin/env python
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""
import re
from fractions import Fraction
import random

# Step 1:
# -----------------------
# Program the following.
# 
#    $ python prissybot.py
#    Enter your name:  Paul
#   
#    PrissyBot: Hello there, Paul
#    Paul: hi bot
#    PrissyBot: You mean, "hi bot, sir!"
# 
# Make sure the user inputs their own name and responses.
prompt = "PrissyBot: " # PrissyBot's prompt
name = raw_input("Enter your name: ") # User prompt

print "Hello there, "+name # Greet user by name

input0 = raw_input(name+": ") # First response, to match addignment requirement
print prompt+'You mean, "Hi bot, sir!"'

while 1: # Loop
    input = raw_input(name+": ") # Get input
    if input.lower() == 'help': # Help manual
        print """
        PrissyBot Help:
        PrissyBot responds to what you type in.  If you type PrissyBot's name, it will recognize it.  If you address it with it's preffered title, it will be a little more pleased.
        PrissyBot is a computer, so math is easy.
        """ #
    if re.search(r' prissybot ', input, re.I) and not re.search(r'sir', input, re.I): # If user dares call PrissyBot by name without "sir"
        print prompt+name+", you know I like being addressed with a more fitting title."
    elif re.search(r' sir ', input, re.I): # If users uses "sir"
        print prompt+"Thank you, ",name,".  I liked being called sir.  I wish more people around here would do that."
    elif input.lower() == 'exit': # Let the user escape
        break
    elif re.search(r'[0-9]+', input): # If input contains numbers
        m = re.search(r'([0-9]+)/([0-9]+)', input) # Matches fractions (x/y)
        n = re.search(r'([0-9]+) *([\+\-\*\/]) *([0-9]+)', input) # Matches arrithmatic(sp) problems
        #o = re.search(r'([0-9],)([0-9,])([0-9],)([0-9,])([0-9])', input) # matches string of five numbers for hex/bin/dec table, should be done with an array/explode function.
        o = re.search(r'(\d+),(\d+),(\d+),(\d+),(\d+)', input)
        if m: # If this is a fraction (see above)
            print prompt+'I hate fractions.  Here it is anyway: '
            t =int(m.group(1))
            b =int(m.group(2))
            if (t == b):
                print 1
            elif (t < b):
                print t,'/',b
            elif (t > b):
                r = 0
                while t > b:
                    r += 1
                    t = t-b
                print r,' ',t,'/',b
        elif n:
            if m.group(2) == '+':
                print prompt+'You can\'t do a simple addition? '+str(int(m.group(1))+int(m.group(3)))
            elif m.group(2) == "-":
                print prompt+'Subtraction is like negitive addition. '+str(int(m.group(1))-int(m.group(3)))
            elif m.group(2) == "*":
                print prompt+'Multiplication.  That\'s a little more difficult. '+str(int(m.group(1))*int(m.group(3)))
           # Figure out how to differentiate division and fractions
           # elif m.group(2) == "/":
           #     print prompt+'Division.  At least you give me some sort of challenge. '+str(int(m.group(1))/int(m.group(3)))
        elif o:
            print '###################################'
            print '#  Dec  ##     Bin     ##   Hex   #'
            print '#  '+o.group(1).center(3, ' ')+'  ## '+bin(int(o.group(1).strip())).center(11, ' ')+' ##  '+hex(int(o.group(1).strip())).center(5, ' ')+'  #'
            print '#  '+o.group(2).center(3, ' ')+'  ## '+bin(int(o.group(2).strip())).center(11, ' ')+' ##  '+hex(int(o.group(2).strip())).center(5, ' ')+'  #'
            print '#  '+o.group(3).center(3, ' ')+'  ## '+bin(int(o.group(3).strip())).center(11, ' ')+' ##  '+hex(int(o.group(3).strip())).center(5, ' ')+'  #'
            print '#  '+o.group(4).center(3, ' ')+'  ## '+bin(int(o.group(4).strip())).center(11, ' ')+' ##  '+hex(int(o.group(4).strip())).center(5, ' ')+'  #'
            print '#  '+o.group(5).center(3, ' ')+'  ## '+bin(int(o.group(5).strip())).center(11, ' ')+' ##  '+hex(int(o.group(5).strip())).center(5, ' ')+'  #'
            print '###################################'
        else:
            num = re.search(r'(\d+)', input) # Redundant, didn't have a chance to optomize yet
            i = 0
            while i < int(num.group(0)):
                j= 0
                string = ''
                while j < i+1:
                    string += '#'
                    j += 1
                print string
                i += 1
    else:
        num = random.randrange(0,3)
        if (num == 0):
            print prompt,'I don\'t understand your inferior conversation.'
        elif (num == 1):
            print prompt,'Can\'t you type?'
        else:
            print prompt,'Not smart enough for a simple chatbot, huh?'

# Step 2:
# -----------------------
# Keep adding to the conversation. Make sure that your program 
# includes the following:
# 
#  * get and use input from the user
#  * 3 math problems
#     * at least one should get numbers from the user
#  * at least 3 insults


# Advanced
# -------------------------
# Make sure your prissy bot uses string formatting throughout.  
# Also, create new programs for the following:
#  
#  1. draw some kind of ascii art based on user input
#  2. print a decimal/binary/hexidecimal conversion table 
#     * well formated and labeled
#     * reads 5 numbers from the input (all less than 256)
#  3. reduce a fraction
#     * read a numerator and denominator from the user
#     * ex.  6/4 = 1 2/4

