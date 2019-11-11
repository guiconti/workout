import math
import os
import random
import re
import sys
import queue

class Node:
    def __init__(self, goal, xPosition, yPosition):
        self.goal = goal
        self.x = xPosition
        self.y = yPosition
        self.visited = False
        self.distance = 0
        self.neighbours = []
    
    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def getNeighbours(self):
        return self.neighbours

def createGraph(grid, goalX, goalY):
    graph = [False] * len(grid)
    for i in range(len(graph)):
        graph[i] = [False] * len(grid[i])

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            isGoal = j == goalX and i == goalY
            print('Start')
            if not graph[i][j]:
                graph[i][j] = Node(isGoal, i, j)

            if grid[i][j] != 'X':
                if (i > 0 and grid[i - 1][j] != 'X'):
                    print('Neighbour', i - 1, j)
                    if not graph[i - 1][j]:
                        isGoal = j == goalX and i - 1 == goalY
                        graph[i - 1][j] = Node(isGoal, i - 1, j)
                    graph[i][j].addNeighbour(graph[i - 1][j])
                    # if (j > 0 and grid[i - 1][j - 1] != 'X'):
                    #     print('Neighbour', i - 1, j - 1)
                    #     if not graph[i - 1][j - 1]:
                    #         isGoal = j - 1 == goalX and i - 1 == goalY
                    #         graph[i - 1][j - 1] = Node(isGoal)
                    #     graph[i][j].neighbours.append(graph[i - 1][j - 1])
                    # if (j < len(grid[i]) - 1 and grid[i - 1][j + 1] != 'X'):
                    #     print('Neighbour', i - 1, j + 1)
                    #     if not graph[i - 1][j + 1]:
                    #         isGoal = j + 1 == goalX and i - 1 == goalY
                    #         graph[i - 1][j + 1] = Node(isGoal)
                    #     graph[i][j].neighbours.append(graph[i - 1][j + 1])
                
                if (i < len(grid) - 1 and grid[i + 1][j] != 'X'):
                    print('Neighbour', i + 1, j)
                    if not graph[i + 1][j]:
                        isGoal = j == goalX and i + 1 == goalY
                        graph[i + 1][j] = Node(isGoal, i + 1, j)
                    graph[i][j].addNeighbour(graph[i + 1][j])
                    # if (j > 0 and grid[i + 1][j - 1] != 'X'):
                    #     print('Neighbour', i + 1, j - 1)
                    #     if not graph[i + 1][j - 1]:
                    #         isGoal = j - 1 == goalX and i + 1 == goalY
                    #         graph[i + 1][j - 1] = Node(isGoal)
                    #     graph[i][j].neighbours.append(graph[i + 1][j - 1])
                    # if (j < len(grid[i]) - 1 and grid[i + 1][j + 1] != 'X'):
                    #     print('Neighbour', i + 1, j + 1)
                    #     if not graph[i + 1][j + 1]:
                    #         isGoal = j + 1 == goalX and i + 1 == goalY
                    #         graph[i + 1][j + 1] = Node(isGoal)
                    #     graph[i][j].neighbours.append(graph[i + 1][j + 1])
                
                if (j > 0 and grid[i][j - 1] != 'X'):
                    print('Neighbour', i, j - 1)
                    if not graph[i][j - 1]:
                        isGoal = j - 1 == goalX and i == goalY
                        graph[i][j - 1] = Node(isGoal, i, j - 1)
                    graph[i][j].addNeighbour(graph[i][j - 1])

                if (j < len(grid[i]) - 1 and grid[i][j + 1] != 'X'):
                    print('Neighbour', i, j + 1)
                    if not graph[i][j + 1]:
                        isGoal = j + 1 == goalX and i == goalY
                        graph[i][j + 1] = Node(isGoal, i, j + 1)
                    graph[i][j].addNeighbour(graph[i][j + 1])

    return graph

def BFS(graph, startX, startY):
    currentQueue = queue.Queue(maxsize = 0)
    currentQueue.put(graph[startX][startY])
    while not currentQueue.empty():
        currentNode = currentQueue.get()
        currentNode.visited = True
        if currentNode.goal:
            return currentNode.distance
        for neighbour in currentNode.getNeighbours():
            if not neighbour.visited:
                neighbour.distance = currentNode.distance + 1
                currentQueue.put(neighbour)
    return -1



# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    graph = createGraph(grid, goalX, goalY)
    return BFS(graph, startX, startY)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
