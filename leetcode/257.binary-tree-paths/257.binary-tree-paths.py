# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def getPaths(self, node: TreeNode, currentPath: str, paths: List[str]):
    if node == None:
      return
    currentPath += f"->{node.val}"
    if not node.left and not node.right:
      paths.append(currentPath)
      return
    self.getPaths(node.left, currentPath, paths)
    self.getPaths(node.right, currentPath, paths)

  def binaryTreePaths(self, root: TreeNode) -> List[str]:
    if root == None:
      return []
    currentPath = str(root.val)
    if not root.left and not root.right:
      return [currentPath]
    paths = []
    self.getPaths(root.left, currentPath, paths)
    self.getPaths(root.right, currentPath, paths)
    return paths