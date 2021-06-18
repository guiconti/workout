# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def invertTreeT(self, root: TreeNode):
    if root is None:
      return None
    temp = root.left
    root.left = root.right
    root.right = temp
    self.invertTreeT(root.left)
    self.invertTreeT(root.right)
  def invertTree(self, root: TreeNode) -> TreeNode:
    self.invertTreeT(root)
    return root