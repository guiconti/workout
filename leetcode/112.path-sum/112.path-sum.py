# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def A(self, root: TreeNode, currentSum: int, targetSum: int) -> bool:
    if not root:
      return False
    currentSum += root.val
    if not root.left and not root.right:
      return currentSum == targetSum
    if root.left and self.A(root.left, currentSum, targetSum):
      return True
    if root.right:
      return self.A(root.right, currentSum, targetSum)
    return False
  def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    if not root:
      return False
    if not root.left and not root.right:
      return root.val == targetSum
    return self.A(root.left, root.val, targetSum) or self.A(root.right, root.val, targetSum)