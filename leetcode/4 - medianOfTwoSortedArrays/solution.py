# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.
# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0

# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    start = 0
    biggestArray, smallestArray = nums1, nums2
    if len(nums1) < len(nums2):
      biggestArray = nums2
      smallestArray = nums1
    end = len(smallestArray)
    
    if len(smallestArray) == 0:
      if len(biggestArray) % 2 == 0:
        return (biggestArray[(len(biggestArray) // 2) - 1] + biggestArray[len(biggestArray) // 2]) / 2
      else:
        return biggestArray[(len(biggestArray) // 2)]
      
    while start <= end:
      partitionX = (start + end) // 2
      partitionY = ((len(biggestArray) + len(smallestArray) + 1) // 2) - partitionX
      print(start, end, partitionX, partitionY)
      
      maxLeftX = -sys.maxsize if partitionX == 0 else smallestArray[partitionX - 1]
      minRightX = sys.maxsize if partitionX == len(smallestArray) else smallestArray[partitionX]
      maxLeftY = -sys.maxsize if partitionY == 0 else biggestArray[partitionY - 1]
      minRightY = sys.maxsize if partitionY == len(biggestArray) else biggestArray[partitionY]
        
      if maxLeftX <= minRightY and maxLeftY <= minRightX:
        if (len(biggestArray) + len(smallestArray)) % 2 == 0:
          return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
        else:
          return max(maxLeftX, maxLeftY)
      elif maxLeftX > minRightY:
        end = partitionX - 1
      else:
        start = partitionX + 1
          