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

# Solution 1 in order print them check if array is sorted. Takes a little of extra memory
# Though it does not validate scenarios where we have two equals values in the root and in the right child
# Works if the tree does not have duplicate values
def inOrderPrint(root, result):
  if not root:
    return result
  
  result = inOrderPrint(root.left, result)
  result.append(root.data)
  result = inOrderPrint(root.right, result)
  return result

# Solution 2 for each sub tree check if the min value of the left sub tree is less or equals than the root
# and for the right sub tree check if the max value is greater than the root
def checkBST(root, minValue, maxValue):
  if not root:
    return True

  if (minValue and root.data <= minValue) or (maxValue and root.data > maxValue):
    return False

  if not checkBST(root.left, minValue, root.data) or not checkBST(root.right, root.data, maxValue):
    return False

  return True

if __name__ == '__main__':
  sortedArray = [1, 2, 3, 4, 5, 6, 7, 8]

  root = createSubTree(None, sortedArray)
  result = inOrderPrint(root, [])
  for i in range(len(result) - 1):
    if result[i] > result[i + 1]:
      print (False)
  print (True)
  print (checkBST(root, None, None))
  
