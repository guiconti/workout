# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def constructSubTree(self, nums: List[int], left: int, right: int):
    if left > right:
      return None
    middle = (left + right) // 2
    root = TreeNode(nums[middle])
    root.left = self.constructSubTree(nums, left, middle - 1)
    root.right = self.constructSubTree(nums, middle + 1, right)
    return root
  def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    return self.constructSubTree(nums, 0, len(nums) - 1)