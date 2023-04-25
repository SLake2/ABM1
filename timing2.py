# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:20:29 2023

@author: LakeS2
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:01:53 2023

@author: LakeS2
"""
import random
import math

# Number of agents is 10 - trialled 500, 1000, 4000, 3...
n_agents = 4

# Initialise these agents
agents = []
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
#print(agents)
    
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
#print(agents)
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
#print("diff x =", dx)

# Calculate the difference in the y coordinates

#print("difference y", y0 - y1)
# or
dy = y0 - y1
#print("diff y", dy)

print()
# Square the differences and add the squares using ** 2
# Could also do manually timesed by each other

#print("Square x", 3**2)
#print("Square y", 4**2)
#or
#print("Square x", dx * dx)
#print("Square y", dy * dy)

print()
# Could square by doing difference x * difference x

#ds = (3**2) + (4**2)
#print("Squares added =", ds)
# or
ds = (dx * dx) + (dy *dy)
#print("Difference squared =", ds)

print()

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



# Get max distance of all
def get_max_distance():
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i + 1, len(agents)):
            b = agents[j]
            print("i", i, "j", j)
            distance = get_distance(a[0], a[1], b[0], b[1])
            max_distance = max(max_distance, distance)
    return max_distance
 
print("Max =", get_max_distance())