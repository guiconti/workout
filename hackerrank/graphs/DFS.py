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

def createGraph(grid):
    graph = [False] * len(grid)
    for i in range(len(graph)):
        graph[i] = [False] * len(grid[i])

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not graph[i][j]:
                graph[i][j] = Node(grid[i][j])

            if graph[i][j].value == 1:
                if i > 0:
                    if grid[i - 1][j] == 1:
                        if not graph[i - 1][j]:
                            graph[i - 1][j] = Node(grid[i - 1][j])
                        graph[i][j].neighbours.append(graph[i - 1][j])
                    if (j > 0 and grid[i - 1][j - 1] == 1):
                        if not graph[i - 1][j - 1]:
                            graph[i - 1][j - 1] = Node(grid[i - 1][j - 1])
                        graph[i][j].neighbours.append(graph[i - 1][j - 1])
                    if (j < len(grid[i]) - 1 and grid[i - 1][j + 1] == 1):
                        if not graph[i - 1][j + 1]:
                            graph[i - 1][j + 1] = Node(grid[i - 1][j + 1])
                        graph[i][j].neighbours.append(graph[i - 1][j + 1])
                
                if (i < len(grid) - 1):
                    if (grid[i + 1][j] == 1):
                        if not graph[i + 1][j]:
                            graph[i + 1][j] = Node(grid[i + 1][j])
                        graph[i][j].neighbours.append(graph[i + 1][j])
                    if (j > 0 and grid[i + 1][j - 1] == 1):
                        if not graph[i + 1][j - 1]:
                            graph[i + 1][j - 1] = Node(grid[i + 1][j - 1])
                        graph[i][j].neighbours.append(graph[i + 1][j - 1])
                    if (j < len(grid[i]) - 1 and grid[i + 1][j + 1] == 1):
                        if not graph[i + 1][j + 1]:
                            graph[i + 1][j + 1] = Node(grid[i + 1][j + 1])
                        graph[i][j].neighbours.append(graph[i + 1][j + 1])
                
                if (j > 0 and grid[i][j - 1] == 1):
                    if not graph[i][j - 1]:
                        graph[i][j - 1] = Node(grid[i][j - 1])
                    graph[i][j].neighbours.append(graph[i][j - 1])

                if (j < len(grid[i]) - 1 and grid[i][j + 1] == 1):
                    if not graph[i][j + 1]:
                        graph[i][j + 1] = Node(grid[i][j + 1])
                    graph[i][j].neighbours.append(graph[i][j + 1])
    return graph

def getClusterSize(currentNode):
    currentClusterSize = DFS(currentNode)
    return currentClusterSize

def DFS(currentNode):
    currentNode.visited = True
    clusterSize = 1
    for neighbour in currentNode.neighbours:
        if not neighbour.visited:
            clusterSize += DFS(neighbour)
    return clusterSize

# Complete the maxRegion function below.
def maxRegion(grid):
    graph = createGraph(grid)
    biggestClusterSize = 0
    print(len(graph[2][3].neighbours))
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j].value == 1 and not graph[i][j].visited:
                clusterSize = getClusterSize(graph[i][j])
                if clusterSize > biggestClusterSize:
                    biggestClusterSize = clusterSize
    return biggestClusterSize

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
