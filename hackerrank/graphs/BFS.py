import math
import os
import random
import re
import sys
import queue

TRAVEL_EFFORT = 6

class Node:
    def __init__(self, index):
        self.index = index
        self.visited = False
        self.distance = 0
        self.neighbours = []

def createGraph(size, connections):
    graph = [0] * size

    for i in range(size):
        graph[i] = Node(i + 1)

    for i in range(len(connections)):
        graph[connections[i][0] - 1].neighbours.append(graph[connections[i][1] - 1])
        graph[connections[i][1] - 1].neighbours.append(graph[connections[i][0] - 1])

    return graph

def BFS(graph, startPosition):
    result = [-1] * (len(graph) - 1)
    graphQueue = queue.Queue(maxsize = 0)
    graphQueue.put(graph[startPosition - 1])

    while not graphQueue.empty():
        currentNode = graphQueue.get()
        currentNode.visited = True
        for neighbour in currentNode.neighbours:
            if not neighbour.visited:
                neighbour.distance = currentNode.distance + TRAVEL_EFFORT
                if neighbour.index > startPosition:
                    result[neighbour.index - 2] = neighbour.distance
                else:
                    result[neighbour.index - 1] = neighbour.distance
                graphQueue.put(neighbour)
    return result


def solution(size, connections, startPosition):
    graph = createGraph(size, connections)
    result = BFS(graph, startPosition)
    return result

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    connections = [0] * m
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        connections[i] = [x, y]
    s = int(input())
    print(' '.join(map(str, solution(n, connections, s))))

