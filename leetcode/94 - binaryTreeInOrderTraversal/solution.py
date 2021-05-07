# 94. Binary Tree Inorder Traversal
# Medium

# 2319

# 98

# Add to List

# Share
# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive solution
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

# Iterative solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    answer = []
    stack = []
    currentNode = root
    
    while currentNode or len(stack) > 0:
      while currentNode:
        stack.append(currentNode)
        currentNode = currentNode.left
      currentNode = stack.pop()
      answer.append(currentNode.val)
      currentNode = currentNode.right
      
    return answer