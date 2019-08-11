#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:34:01 2019

@author: evangelos
"""

# The chaos game. See wikipedia.org/wiki/Chaos_game for more information.

import numpy as np
import matplotlib.pyplot as plt

# Set the coordinates of the vertices
p1 = (0, 0)
p2 = (10, 0)
p3 = (5, np.sqrt(75))

# Choose the number of iterations
iterations = 100000

# This array will be used to save the coordinates of the cursor after every iteration
points = np.zeros((iterations, 2))

# Set the starting point
points[0, :] = (np.random.randint(0, 10+1), np.random.randint(0, 10+1))
#points[0, :] = (0, 0)
#points[0, :] = (5, 2.5)

# Play!
for i in np.arange(1, iterations):
    throw = np.random.randint(1, 3+1)
    if throw==1:
        points[i, 0] = (p1[0] + points[i-1, 0]) / 2
        points[i, 1] = (p1[1] + points[i-1, 1]) / 2
    elif throw==2:
        points[i, 0] = (p2[0] + points[i-1, 0]) / 2
        points[i, 1] = (p2[1] + points[i-1, 1]) / 2
    elif throw==3:
        points[i, 0] = (p3[0] + points[i-1, 0]) / 2
        points[i, 1] = (p3[1] + points[i-1, 1]) / 2

# Plot the results
plt.figure(10)
plt.clf()
plt.plot(points[:, 0], points[:, 1], 'bv', ms=0.5)
plt.plot(points[0, 0], points[0, 1], 'r+')
plt.show()
