class Node:
  left, right = None, None
  def __init__(self, index, left, right):
    self.index = index
    self.left = left
    self.right = right

def inOrderTraverse(currentNode, result):

  if currentNode == None:
    return result

  result = inOrderTraverse(currentNode.left, result)
  result.append(currentNode.index)
  result = inOrderTraverse(currentNode.right, result)
  return result

if __name__ == '__main__':
  root = Node(8, None, None)
  root.left = Node(6, None, None)
  root.left.left = Node(5, None, None)
  root.left.right = Node(7, None, None)
  root.right = Node(12, None, None)
  root.right.left = Node(11, None, None)
  root.right.right = Node(13, None, None)
  result = inOrderTraverse(root, [])
  print (result)