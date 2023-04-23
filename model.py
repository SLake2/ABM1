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
if rn > 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
print("y0", y0)

# note: Can change the random seed to another variable if wanted
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

# Calculate the difference in the x coordinates. 
#Use abs(x0-x1) for x values and same but replace for y

print("difference x", abs(x0-x1))

# Calculate the difference in the y coordinates

print("difference y", abs(y0-y1))

# Square the differences and add the squares using ** 2

print("Square x", 3**2)
print("Square y", 4**2)

print("Squares added =", 9+16)

# Calculate the square root (using ** 0.5)
print("Square Root =", 25**0.5)

print("The difference between the coordinates [0,0] and [3,4] is 5.")