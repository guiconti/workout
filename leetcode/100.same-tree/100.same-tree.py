# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def checkNode(self, p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
      return True
    if p is None and not q is None:
      return False
    if not p is None and q is None:
      return False
    if not self.checkNode(p.left, q.left):
      return False
    if p.val != q.val:
      return False
    return self.checkNode(p.right, q.right) 
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    return self.checkNode(p, q)