#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = int(raw_input("Enter a number: "))

if n%2 == 0:
    nType = "Even"
else:
    nType = "Odd"

print "1.",nType


# 2. If n is odd, double it
# If n is supposed to be changed by this and following calulations, set the below to False.  If n should remain unchanged for questions 3 and 4, leave True.
preserveN = True

if nType == "Odd":
    if preserveN == True:
        n2 = n*2
        print "2. ",n2
    else:
        n = n*2
        print "2. ",n
else:
    print "2. Skip me!"

# 3. If n is evenly divisible by 3, add four
if  n%3 == 0:
    if preserveN == True:
        n3 = n+4
        print "3.",n3
    else:
        n += 4
        print "3. ",n
else:
    print "3. Skip me!"

# 4. What is grade's letter value (eg. 90-100)
# While a good programming practice, my inner Hampshire student is offended by the lack of eval option
# (And my inner programmer is having trouble with switch statments)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

if grade > 90:
    letter = "A"
elif grade > 80:
    letter = "B"
elif grade > 70:
    letter = "C"
else:
    letter = "F"

print "4.",letter
