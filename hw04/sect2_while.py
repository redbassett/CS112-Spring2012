#!/usr/bin/env python
from hwtools import *

print "Section 2:  Loops"
print "-----------------------------"

# 1. Keep getting a number from the input (num) until it is a multiple of 3.
num = 0
escape = False

while escape == False:
    num = int(raw_input("Enter a number: "))
    if num != 0 and num%3 == 0:
        escape = True

print "1.", num

# 2. Countdown from the given number to 0 by threes. 
#    Example:
#      12...
#      9...
#      6...
#      3...
#      0

print "2. Countdown from", num
while num >= 0:
    print num
    num -= 3


# 3. [ADVANCED] Get another num.  If num is a multiple of 3, countdown 
#    by threes.  If it is not a multiple of 3 but is even, countdown by 
#    twos.  Otherwise, just countdown by ones.

num = int(raw_input("3. Countdown from: "))

if num % 3 == 0:
    while num >= 0:
        print num
        num -= 3
elif num % 2 == 0:
    while num >= 0:
        print num
        num -= 2
else:
    while num >= 0:
        print num
        num -= 1
