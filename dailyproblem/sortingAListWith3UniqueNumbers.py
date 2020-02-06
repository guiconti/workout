# Hi, here's your problem today. This problem was recently asked by Google:

# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

# Example 1:
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]
def sortNums(nums):
  count = [0] * 3
  for i in range(len(nums)):
    count[nums[i] - 1] += 1
  for i in range(0, count[0]):
    nums[i] = 1
  for i in range(count[0], count[0] + count[1]):
    nums[i] = 2
  for i in range(count[0] + count[1], len(nums)):
    nums[i] = 3

  return nums

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]