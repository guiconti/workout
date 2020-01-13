# 42. Trapping Rain Water
# Hard

# 5313

# 104

# Add to List

# Share
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution:
  def trap(self, height: List[int]) -> int:
    answer = 0
    size = len(height)
    if size == 0:
      return 0
    maxLeft = [0] * size
    maxRight = [0] * size
    
    maxLeft[0] = height[0]
    for i in range(1, size):
      maxLeft[i] = max(height[i], maxLeft[i - 1])
    
    maxRight[size - 1] = height[size - 1]
    for i in range(size - 2, -1, -1):
      maxRight[i] = max(height[i], maxRight[i + 1])
      
    for i in range(1, size - 1):
      answer += min(maxLeft[i], maxRight[i]) - height[i]
      
    return answer
      