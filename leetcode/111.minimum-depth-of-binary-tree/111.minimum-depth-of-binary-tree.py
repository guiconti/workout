# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def getDepth(self, root: TreeNode, currentDepth: int) -> int:
    if not root:
      return currentDepth
    currentDepth += 1
    if not root.left:
      return self.getDepth(root.right, currentDepth)
    if not root.right:
      return self.getDepth(root.left, currentDepth)
    return min(self.getDepth(root.left, currentDepth), self.getDepth(root.right, currentDepth))
  def minDepth(self, root: TreeNode) -> int:
    return self.getDepth(root, 0)