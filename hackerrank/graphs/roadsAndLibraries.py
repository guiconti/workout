#!/bin/python3

import math
import os
import random
import re
import sys

class Node:
    def __init__(self):
        self.visited = False
        self.neighbours = []

def createGraph(size, connections):
    graph = [0] * size

    for i in range(size):
        graph[i] = Node()

    for i in range(len(connections)):
        graph[connections[i][0] - 1].neighbours.append(graph[connections[i][1] - 1])
        graph[connections[i][1] - 1].neighbours.append(graph[connections[i][0] - 1])
    
    return graph

def findClusterSize(currentNode):
    clusterSize = DFS(currentNode, 1)
    print (clusterSize)
    return clusterSize

def DFS(currentNode, currentSize):
    currentNode.visited = True
    for neighbour in currentNode.neighbours:
        if not neighbour.visited:
            currentSize = 1 + DFS(neighbour, currentSize)
    return currentSize

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib
    
    graph = createGraph(n, cities)
    totalCost = 0

    for node in graph:
        if not node.visited:
            clusterSize = findClusterSize(node)
            totalCost += ((clusterSize - 1) * c_road) + c_lib

    return totalCost
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
