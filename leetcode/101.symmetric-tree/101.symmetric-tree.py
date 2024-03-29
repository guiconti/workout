# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def ValidateNodes(self, nodeA, nodeB) -> str:
    if not nodeA or not nodeB:
      return nodeA == nodeB
    return nodeA.val == nodeB.val and self.ValidateNodes(nodeA.left, nodeB.right) and self.ValidateNodes(nodeA.right, nodeB.left)
  def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
      return False
    return self.ValidateNodes(root.left, root.right)