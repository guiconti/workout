class Solution:
  def preorder(self, root: TreeNode, result: List[int]) -> List[int]:
    if not root:
      return result
    result.append(root.val)
    self.preorder(root.left, result)
    self.preorder(root.right, result)
    return result
  def preorderTraversal(self, root: TreeNode) -> List[int]:
    return self.preorder(root, [])

# Iterative version
# class Solution:
#   def preorderTraversal(self, root: TreeNode) -> List[int]:
#     if not root:
#       return []
#     result = []
#     nodeStack = []
#     nodeStack.append(root)

#     while (len(nodeStack) > 0):
#       node = nodeStack.pop()
#       result.append(node.val)

#       if node.left:
#         nodeStack.append(node.left)
#       if node.right:
#         nodeStack.append(node.right)
#     return result