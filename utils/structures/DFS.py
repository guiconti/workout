#!/bin/python3

import math
import os
import random
import re
import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.neighbours = []

def createGraph(size, connections):
    graph = [0] * size

    for i in range(size):
        graph[i] = Node(i + 1)

    for i in range(len(connections)):
        graph[connections[i][0] - 1].neighbours.append(graph[connections[i][1] - 1])
        graph[connections[i][1] - 1].neighbours.append(graph[connections[i][0] - 1])

    return graph

def DFS(currentNode):
    currentNode.visited = True
    clusterSize = 1
    for neighbour in currentNode.neighbours:
        if not neighbour.visited:
            clusterSize += DFS(neighbour)
    return clusterSize   

if __name__ == '__main__':
    graph = createGraph(5, [[1,2], [1, 3], [2, 5], [3, 4], [3, 5], [4, 5]]) 
    print(DFS(graph[0]))
