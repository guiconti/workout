# Given a graph find if there is a route between two nodes

import queue

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

def covers(root, value):
  if not root:
    return False
  if root.data == value:
    return True
  return covers(root.left, value) or covers(root.right, value)

def findAncestor(root, valueA, valueB):
  if not root or root.data == valueA or root.data == valueB:
    return root
  
  isValueAOnLeft = covers(root.left, valueA)
  isValueBOnLeft = covers(root.left, valueB)

  # If they are not on the same side it means we found a root
  if isValueAOnLeft != isValueBOnLeft:
    return root
  
  childSide = root.left if isValueAOnLeft else root.right
  return findAncestor(childSide, valueA, valueB)

def firstCommonAncestor(root, valueA, valueB):
  # Check if both values are in the tree
  if not covers(root, valueA) or not covers(root, valueB):
    return None
  return findAncestor(root, valueA, valueB)

if __name__ == '__main__':
  sortedArray = [1, 2, 3, 4, 5, 6, 7, 8]

  root = createSubTree(None, sortedArray)
  firstCommonAncestorNode = firstCommonAncestor(root, 6, 7)
  print(firstCommonAncestorNode.data)
  
  
