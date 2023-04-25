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

# ABM2: adding lists for agents

# Create a list for agents
#agents = []
# Add coordinates to list - append to the list agents 
#agents.append([x0, y0])

# Change x0 and y0 randomly
import random

#rn = random.random()
#print("rn", rn)

# if statement
#if rn < 0.5:
#    agents[0][0] = agents[0][0] + 1
#else:
#    agents[0][0] = agents[0][0] - 1

#print("x0", agents[0][0])

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Changge from agent list from the x0,y0 to ranges

# Number of agents is 10
n_agents = 10

# Initialise these agents
agents = []
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
print(agents)
    
# Move agents
for i in range(n_agents):
    # Change agents[i] coordinates randomly
    # x-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    # y-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1
print(agents)


# Same for Y values - try > instead of <
#if rn < 0.5:
#    agents[0][1] = agents[0][1] + 1
#else:
#    agents[0][1] = agents[0][1] - 1
    
#print("y0", agents[0][1])

# note: Can change the random seed to another variable if wanted e.g.random.seed(1)
print()

# note: deleted extra trials for abm2

# Do the same for x1 and y1 variables
x1 = 1
print("x1", x1)

y1 = 1
print("y1", y1)


import random

rn = random.random()

print("rn2", rn)

if rn > 0.5:
    x1 = x1 + 1
else:
    x1 - 1

print("x1", x1)

if rn < 0.5:
   y1 = y1 + 1
else:
    y1 = y1 - 1

print("y1", y1)

# New space for next part of ABM
print()

# ABM 1 No. 4
# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# A sqr + B sqr = C sqr

# Add to source code x0 and y0 = 0 and x1 = 3 and y1 = 4

x0 = 0
y0 = 0
x1 = 3
y1 = 4

print() # new space for visulaisation

# ABM 2 - add x1 and y1 to agents list and change code to recognise this
#agents.append([x1, y1])


# Calculate the difference in the x coordinates. 
# Could just do x0 - x1 or y0 - y1

#print("difference x", x0 - x1)
# or
dx = x0 - x1
print("diff x =", dx)

# Calculate the difference in the y coordinates

#print("difference y", y0 - y1)
# or
dy = y0 - y1
print("diff y", dy)

print()
# Square the differences and add the squares using ** 2
# Could also do manually timesed by each other

#print("Square x", 3**2)
#print("Square y", 4**2)
#or
print("Square x", dx * dx)
print("Square y", dy * dy)

print()
# Could square by doing difference x * difference x

#ds = (3**2) + (4**2)
#print("Squares added =", ds)
# or
ds = (dx * dx) + (dy *dy)
print("Difference squared =", ds)

print()
# Calculate the square root (using ** 0.5)
#print("Square Root =", 25**0.5)
#print("Distance =", ds**0.5)
#only if using the second options in all these examples

# Or could import math and do the square root this way
# print("The difference in distance between the coordinates [0,0] and [3,4] is 5.")

# ABM 2 - Plotting

# Plotting the agents
import matplotlib.pyplot as plt
import operator

# Make a scatter plot showing the coordinates
#plt.scatter(agents[0][0], agents[0][1], color='black')
#plt.scatter(agents[1][0], agents[1][1], color='black')
#plt.show()

# Get the coordinates with the largest x-coordinate
#print(max(agents, key=operator.itemgetter(0)))

# Plot point with largest x-coordinate in red

# Manually change what you know has the largest x coordinate from the print above
#plt.scatter(agents[0][0], agents[0][1], color='black')
#plt.scatter(agents[1][0], agents[1][1], color='red')

# Doing it with code/automatically trials
#plt.scatter(agents[0][0], agents[0][1], color='black')

# Plotting ranged agents
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')

#lx = largest x value, use the code provided for print and then  plot this with colour changed
lx = (max(agents, key=operator.itemgetter(0)))
plt.scatter(lx[0], lx[1], color='red')

# smallest x value in blue, largest y in yellow and smallest y in green
sx = (min(agents, key=operator.itemgetter(0)))
plt.scatter(sx[0], sx[1], color='blue')
ly= (max(agents, key=operator.itemgetter(1)))
plt.scatter(ly[0], ly[1], color='yellow')
sy= (min(agents, key=operator.itemgetter(1)))
plt.scatter(sy[0], sy[1], color='green')
plt.show()

print()
# ABM 3 - Changing distance and Max Distance calulations

# Get Distance use - first define it, then parameters 

def get_distance(x0, y0, x1, y1):
    """
   Calculate the Euclidean distance between (x0, y0) and (x1, y1).

   Parameters
   ----------
   x0 : Number
       The x-coordinate of the first coordinate pair.
   y0 : Number
       The y-coordinate of the first coordinate pair.
   x1 : Number
       The x-coordinate of the second coordinate pair.
   y1 : Number
       The y-coordinate of the second coordinate pair.

   Returns
   -------
   distance : Number
       The Euclidean distance between (x0, y0) and (x1, y1).
   """
   # Calculate the difference in the x coordinates.
    dx = x0 - x1
   # Calculate the difference in the y coordinates.
    dy = y0 - y1
   # Return the Sum the squared differences square rooted.
    return((dx * dx) + (dy *dy)) **0.5
print("Distance =", ((dx * dx) + (dy *dy)) **0.5)
print()


# Max distance initilisation - taken out for ease
#max_distance = 0 
#for a in agents:
#    for b in agents:
#        distance = get_distance(a[0], a[1], b[0], b[1])
#        print("distance between", a, b, distance)
#        max_distance = max(max_distance, distance)
#        print("max_distance", max_distance)
        
# Also can be done by
max_distance = 0

for i in range(len(agents)):
    a = agents[i]
    for j in range(len(agents)):
        b = agents[j]
        distance = get_distance(a[0], a[1], b[0], b[1])
        print("distance between", a, b, distance)
        max_distance = max(max_distance, distance)
        print("max_distance", max_distance)

print()
# Get max distance of all
def get_max_distance(x0, y0, x1, y1):
     """ 
     Calulating maximum distance between all agents
     Parameters again x0, y0, x1, y1
     Returns distance: number
     """
     #calculate the maximum distance between all agents
     return(max(max_distance, distance))
print("Max_dist_agents", max_distance)
     