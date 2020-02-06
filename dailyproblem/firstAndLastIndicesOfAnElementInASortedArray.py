# Given a sorted array, A, with possibly duplicated elements
# find the indices of the first and last occurrences of a target element, x.
# Return -1 if the target is not found.

# Example:
# Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: [6,8]

# Input: A = [100, 150, 150, 153], target = 150
# Output: [1,2]

# Input: A = [1,2,3,4,5,6,10], target = 9
# Output: [-1, -1]

# Solution (n)
# The average case could be improved to O(logn) using Binary search
class Solution:
    def getRange(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low < high:
            if arr[low] != target:
                low += 1
            if arr[high] != target:
                high -= 1
            if arr[low] == arr[high] == target:
                return [low, high]

        return [-1, -1]


# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
target = 2
print(Solution().getRange(arr, target))
# [1, 4]

arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
target = 9
print(Solution().getRange(arr, target))
# Output: [6,8]

arr = [100, 150, 150, 153]
target = 150
print(Solution().getRange(arr, target))
# Output: [1,2]

arr = [1, 2, 3, 4, 5, 6, 10]
target = 9
print(Solution().getRange(arr, target))
# Output: [-1, -1]
