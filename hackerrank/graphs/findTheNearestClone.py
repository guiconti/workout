#!/bin/python3

import math
import os
import random
import re
import sys
import queue

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#

class Node:
    def __init__(self, color):
        self.neighbours = []
        self.visited = False
        self.distance = 0
        self.color = color

def createGraph(graph_nodes, graph_from, graph_to, ids):
    graph = [0] * graph_nodes
    for i in range(graph_nodes):
        graph[i] = Node(ids[i])

    for i in range(len(graph_from)):
        graph[graph_from[i] - 1].neighbours.append(graph[graph_to[i] - 1])
        graph[graph_to[i] - 1].neighbours.append(graph[graph_from[i] - 1])

    return graph

def BFS(graph, color):
    graphQueue = queue.Queue(maxsize = 0)
    for node in graph:
        if node.color == color:
            graphQueue.put(node)
            break

    minDistance = -1
    while not graphQueue.empty():
        currentNode = graphQueue.get()
        currentNode.visited = True
        if (currentNode.color == color and currentNode.distance != 0):
            if (minDistance == -1 or currentNode.distance < minDistance):
                minDistance = currentNode.distance
            currentNode.distance = 0
        for neighbour in currentNode.neighbours:
            if not neighbour.visited:
                neighbour.distance = currentNode.distance + 1
                graphQueue.put(neighbour)

    return minDistance

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = createGraph(graph_nodes, graph_from, graph_to, ids)
    return BFS(graph, val)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
