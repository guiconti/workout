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
    leftDepth = self.getDepth(root.left, currentDepth + 1)
    rightDepth = self.getDepth(root.right, currentDepth + 1)
    if leftDepth == -1 or rightDepth == -1 or abs(leftDepth - rightDepth) > 1:
      return -1
    return max(leftDepth, rightDepth)
  def isBalanced(self, root: TreeNode) -> bool:
    if not root:
      return True
    leftDepth = self.getDepth(root.left, 0)
    rightDepth = self.getDepth(root.right, 0)
    return leftDepth > -1 and rightDepth > -1 and abs(leftDepth - rightDepth) <= 1