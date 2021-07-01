# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def isNodeUnderRoot(self, root: TreeNode, node: TreeNode):
    if not root:
      return False
    if root.val == node.val:
      return True
    return self.isNodeUnderRoot(root.left, node) or self.isNodeUnderRoot(root.right, node)

  def findAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root.val == p.val or root.val == q.val:
      return root
    isPOnLeft = self.isNodeUnderRoot(root.left, p)
    isQOnLeft = self.isNodeUnderRoot(root.left, q)
    if isPOnLeft != isQOnLeft:
      return root
    newRoot = root.left if isPOnLeft else root.right
    return self.findAncestor(newRoot, p, q)

  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    return self.findAncestor(root, p, q)