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

def inOrderPrint(root, result):
  if not root:
    return result
  
  result = inOrderPrint(root.left, result)
  result.append(root.data)
  result = inOrderPrint(root.right, result)
  return result

if __name__ == '__main__':
  sortedArray = [1, 2, 3, 4, 5, 6, 7, 8]

  root = createSubTree(None, sortedArray)
  print (inOrderPrint(root, []))
  
