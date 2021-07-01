# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def isNodeUnderRoot(self, root, value):
    if not root:
      return False
    if root.val == value:
      return True
    return self.isNodeUnderRoot(root.left, value) or self.isNodeUnderRoot(root.right, value)

  def findAncestor(self, root, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root.val == p.val or root.val == q.val:
      return root
    isPOnLeft = self.isNodeUnderRoot(root.left, p.val)
    isQOnLeft = self.isNodeUnderRoot(root.left, q.val)
    if isPOnLeft != isQOnLeft:
      return root
    newRoot = root.left if isPOnLeft else root.right
    return self.findAncestor(newRoot, p, q)

  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    return self.findAncestor(root, p, q)