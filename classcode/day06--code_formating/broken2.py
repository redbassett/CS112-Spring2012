#!/usr/bin/env python
from random import randint
s = 1
t = int(raw_input())
rr = []

# For each element between 0 and entered int
for _ in range(t):
    # Add a random int to rr
    rr.append(randint(0,20))
print rr


while s:
    s=0
    for var in range(1,t):
        if rr[var-1]>rr[var]:
            t1=rr[i-1]
            t2=rr[i]
            rr[i-1]=t2
            rr[i]=t1
            s=1
print rr
