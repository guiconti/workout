""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

INT_MAX = 4294967296
INT_MIN = -4294967296

def isBST(node, minValue, maxValue):
    if not node:
        return True
    
    if node.data < minValue and node.data > maxValue:
        return False
    
    return isBST(node.left, minValue, node.data - 1) and isBST(node.right, node.data + 1, maxValue)

def check_binary_search_tree_(root):
    return isBST(root, INT_MIN, INT_MAX)
    