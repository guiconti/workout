# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def fillPaths(self, node: TreeNode, targetSum: int, currentSum: int, currentPath: str, result: List[List[int]]):
    if node == None:
      return
    currentSum += node.val
    currentPath += f",{node.val}"
    if node.left == None and node.right == None:
      if currentSum == targetSum:
        result.append(list(currentPath.split(",")))
      return
    self.fillPaths(node.left, targetSum, currentSum, currentPath, result)
    self.fillPaths(node.right, targetSum, currentSum, currentPath, result)
  def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
    result = []
    if root == None:
      return result
    if root.left == None and root.right == None:
      if root.val == targetSum:
        result.append([root.val])
      return result
    self.fillPaths(root.left, targetSum, root.val, str(root.val), result)  
    self.fillPaths(root.right, targetSum, root.val, str(root.val), result)  
    return result