# Given a binary tree, count the number of uni-value subtrees.

# A Uni-value subtree means all nodes of the subtree have the same value.

# Example :

# Input:  root = [5,1,5,5,5,null,5]

#               5
#              / \
#             1   5
#            / \   \
#           5   5   5

# Output: 4

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def DFS(self, root):
    
    if not root.left and not root.right:
      self.count += 1
      return True
    
    left = right = True
    if root.left:
      left = self.DFS(root.left) and root.left.val == root.val
    if root.right:
      right = self.DFS(root.right) and root.right.val == root.val
    if not left or not right:
      return False
    self.count += 1
    return True
    
  def countUnivalSubtrees(self, root: TreeNode) -> int:
    self.count = 0
    if root:
      self.DFS(root)
    return self.count