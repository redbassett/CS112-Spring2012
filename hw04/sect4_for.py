#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?
total = 0
for num in nums:
    total += num
print "1.",total


# 2. Print every even number in nums
print "2. even numbers"

for num in nums:
    if num%2 == 0:
        print num


# 3. Does nums only contain even numbers? 
only_even = True

for num in nums:
    if num % 2 != 0:
        only_even = False

print "3.",
if only_even:
    print "only even"
else:
    print "some odd"


# 4. Generate a list every odd number less than 100. Hint: use range()
print "4.", range(1, 100, 2)

# 5. [ADVANCED]  Multiply each element in nums by its index
i = 0
for num in nums:
    nums[i] = num * i
    i += 1
print "5.", nums
