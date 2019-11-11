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

def generateDepthLists(root, lists, depth):
  if not root:
    return lists
  
  if len(lists) < depth:
    lists.append([])
  
  lists[depth - 1].append(root.data)
  lists = generateDepthLists(root.left, lists, depth + 1)
  lists = generateDepthLists(root.right, lists, depth + 1)
  return lists

if __name__ == '__main__':
  sortedArray = [1, 2, 3, 4, 5, 6, 7, 8]

  root = createSubTree(None, sortedArray)
  lists = generateDepthLists(root, [], 1)
  print(lists)
  