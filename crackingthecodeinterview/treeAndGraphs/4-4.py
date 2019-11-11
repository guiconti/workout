# Given a graph find if there is a route between two nodes

import queue
import sys

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def createSubTree(root, sortedArray):
  if len(sortedArray) == 0:
    return None
  median = len(sortedArray) // 2
  root = Node(sortedArray[median])
  root.left = createSubTree(root, sortedArray[:median])
  root.right = createSubTree(root, sortedArray[median + 1:])
  return root

def checkHeight(root):
  if not root:
    return -1
  
  leftHeight = checkHeight(root.left)
  if leftHeight == sys.maxsize * -1:
    return sys.maxsize * -1
  rightHeight = checkHeight(root.right)
  if rightHeight == sys.maxsize * -1:
    return sys.maxsize * -1
  
  if abs(leftHeight - rightHeight) > 1:
    return sys.maxsize * -1
  return max(leftHeight, rightHeight) + 1

if __name__ == '__main__':
  sortedArray = [1, 2, 3, 4, 5, 6, 7, 8]

  root = createSubTree(None, sortedArray)
  print (checkHeight(root))

  