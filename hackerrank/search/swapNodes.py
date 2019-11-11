#!/bin/python3

import os
import sys
import queue

class Node:
    left, right = None, None
    index, depth = 0, 0
    def __init__(self, index, depth, left, right):
        self.index = index
        self.depth = depth
        self.left = left
        self.right = right

def printInOrder(currentNode, result):
    if currentNode == None:
        return result
    result = printInOrder(currentNode.left, result)
    result.append(currentNode.index)
    result = printInOrder(currentNode.right, result)
    return result

def swapInOrder(currentNode, depth, k):
    if currentNode == None:
        return
    swapInOrder(currentNode.left, depth + 1, k)
    swapInOrder(currentNode.right, depth + 1, k)

    if depth >= k and depth % k == 0:
        temp = currentNode.left
        currentNode.left = currentNode.right
        currentNode.right = temp

#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    rootNode = Node(1, 1, None, None)
    currentNode = rootNode
    nodeQueue = queue.Queue(maxsize = 0)
    nodeQueue.put(currentNode)

    for i in range(len(indexes)):
        currentNode = nodeQueue.get()
        leftData = indexes[i][0];
        rightData = indexes[i][1];
        if leftData != -1:
            currentNode.left = Node(leftData, currentNode.depth + 1, None, None)
            nodeQueue.put(currentNode.left)
        if rightData != -1:
            currentNode.right = Node(rightData, currentNode.depth + 1, None, None)
            nodeQueue.put(currentNode.right)

    result = []
    for i in range(len(queries)):
        currentResult = []
        swapInOrder(rootNode, 1, queries[i])
        currentResult = printInOrder(rootNode, currentResult)
        result.append(currentResult)

    return result;

if __name__ == '__main__':
    sys.setrecursionlimit(15000)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
