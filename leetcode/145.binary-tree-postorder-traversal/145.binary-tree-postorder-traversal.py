class Solution:
  def postorder(self, root: TreeNode, result: List[int]) -> List[int]:
    if not root:
      return result
    self.postorder(root.left, result)
    self.postorder(root.right, result)
    result.append(root.val)
    return result
  def postorderTraversal(self, root: TreeNode) -> List[int]:
    return self.postorder(root, [])
  
# Iterative
# class Solution:
#   def postorderTraversal(self, root: TreeNode) -> List[int]:
#     current = root
#     nodeStack = []
#     result = []
#     while True:
#       if not current and len(nodeStack) == 0:
#         break
#       if current:
#         nodeStack.append(current)
#         current = current.left
#         continue
#       # len(stack) > 0
#       current = nodeStack.pop()
#       result.append(current.val)
#       current = current.right
#     return result
