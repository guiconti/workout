# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def inOrderTraverse(self, node: TreeNode, result: List[int]) -> List[int]:
    if not node:
      return result
    result = self.inOrderTraverse(node.left, result)
    result.append(node.val)
    result = self.inOrderTraverse(node.right, result)
    return result
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    return self.inOrderTraverse(root, [])