# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:04:36 2023

@author: Sian
"""
# Nos. 2 and 3 of ABM1
# Initialise variable x0
x0 = 0
print("x0", x0)

# Initialise variable y0
y0 = 0
print("y0", y0)

# Change x0 and y0 randomly
import random

rn = random.random()
print("rn", rn)

# if statement
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1

print("x0", x0)

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Same for Y values - try > instead of <
if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
print("y0", y0)

# note: Can change the random seed to another variable if wanted e.g.random.seed(1)
print()
print("New Random Seed trials")
random.seed(1)
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1

print("rs1 x0", x0)

if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
print("rs1 y0", y0)

# With different number than 0 or 1

random.seed(49)
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1

print("rs49 x0", x0)

if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
print("rs49 y0", y0)

# note: also trialled with opposite sign [> instead of oringinal <]

# Seperate the numbers so less cluttered using print function

print()

# Do the same for x1 and y1 variables
x1 = 1
print("x1", x1)

y1 = 1
print("y1", y1)

import random

rn = random.random()

print("rn2", rn)

if rn > 0.5:
    x1 = x1 -1
else:
    x1 = x1 + 1

print("x1", x1)

if rn < 0.5:
    y1 = y1 - 1
else:
    y1 = y1 + 1

print("y1", y1)

# New space for next part of ABM
print()

# No. 4
# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# A sqr + B sqr = C sqr

# Add to source code x0 and y0 = 0 and x1 = 3 and y1 = 4

x0 = 0
y0 = 0
x1 = 3
y1 = 4

# See as coordinates using square brakets
print([x0, y0]) 
print([x1, y1])

print() # new space for visulaisation
 
# Calculate the difference in the x coordinates. 
# Can use abs(x0-x1) for x values and same but replace for y
# Could just do x0 - x1 or y0 - y1

print("difference x", x0 - x1)
# or
difx = x0 - x1
print("diff x =", difx)

# Calculate the difference in the y coordinates

print("difference y", y0 - y1)
# or
dify = y0 - y1
print("diff y", dify)

print()
# Square the differences and add the squares using ** 2
# Could also do manually timesed by each other

print("Square x", 3**2)
print("Square y", 4**2)
#or
print("Square x", difx * difx)
print("Square y", dify * dify)

print()
# Could square by doing difference x * difference x

difference = (3**2) + (4**2)
print("Squares added =", difference)
# or
differencesq = (difx * difx) + (dify *dify)
print("Difference squared =", differencesq)

print()
# Calculate the square root (using ** 0.5)
print("Square Root =", 25**0.5)
print("Distance =", differencesq**0.5)
#only if using the second options in all these examples

# Or could import math and do the square root this way

print("The difference in distance between the coordinates [0,0] and [3,4] is 5.")
