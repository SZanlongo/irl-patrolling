### Convert a reward matrix into a trajectory ###

import math
import matplotlib.pyplot as plt
import numpy as np
import skimage.util as ski
from numpy import average
from _heapq import heappush, heappop

# Read file
def readFile (fname):
    with open(fname) as f:
        lines = f.read().splitlines()
    return lines

# Extract reward values into 
def extractReward(info):
    cellCount = len(info)   # number of cells
    dim = math.sqrt(cellCount)   # assumes dimensions are equal
    reward = np.empty(shape = (dim, dim))  # reward matrix
    
    for i, item in enumerate(info): # copy rewards into corresponding x, y cell
        reward[i % dim, math.floor(i / dim)] = item
    return reward

# Simplify reward matrix by using averages
def simplifyReward(reward, block):
    return ski.view_as_blocks(reward, (block, block)).mean(axis = (2, 3)) # simplified (average) reward matrix

# Find points deemed "high reward"
def getHighReward(simpleReward, offset):
    dim = len(simpleReward)
    avrg = abs(average(simpleReward)) * offset  # consider "high reward" any point that is above average * offset
    path = []

    for x in range(dim):    # iterate over all points and append "high reward" points
        for y in range(dim):
            if (simpleReward[x, y] > avrg):
                path.append([x, y])
            
    return path

# Calculate euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Find greedy path through "high reward" points
def greedyPath(points, start):
    gPath = []  # greedy path
    dist = []   # distance heap
    curr = start
    gPath.append(curr)  # start path with start point
    
    while points:   # while there are points left
        for i, point in enumerate(points):  # get distances from current point to all other points
            heappush(dist, (distance(curr, point), i, point))   # 3-tuple [distance, point index, point coordinates]
            
        nearest = heappop(dist)    # get nearest point
        dist = []   # clear heap
        del points[nearest[1]]    # remove point from points
        curr = nearest[2]  # update current point
        gPath.append(curr)   # append point to greedyPath
    
    gPath.append(start) # return to start
    
    return gPath

# Plot path
def plotPath(path):
    xs = [] # x-coordinates
    ys = [] # y-coordinates
    
    for point in path:  # extract path
        xs.append(point[0])
        ys.append(point[1])
        
    # set up graph and plot path
    plt.ylim([0, 10])
    plt.xlim([0, 10])
    plt.plot(xs, ys)
    plt.suptitle("Patrol Path")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
        
reward = extractReward(readFile("../data/10f.txt")) # original reward matrix
simpleReward = simplifyReward(reward, 5)    # simplified reward matrix
rewardPoints = getHighReward(simpleReward, 1)   # high reward points
gPath = greedyPath(rewardPoints, [0, 0])    # find greedy path
plotPath(gPath) # plot points
