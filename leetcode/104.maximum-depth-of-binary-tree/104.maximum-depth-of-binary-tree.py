# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def getMaxDepth(self, node: TreeNode, currentDepth: int) -> int:
    if not node:
      return currentDepth
    currentDepth += 1
    depthLeft = self.getMaxDepth(node.left, currentDepth)
    depthRight = self.getMaxDepth(node.right, currentDepth)
    if depthLeft > depthRight:
      return depthLeft
    return depthRight
  def maxDepth(self, root: TreeNode) -> int:
    return self.getMaxDepth(root, 0)