class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1 = nums1[:len(nums1)-len(nums2)]
    i = 0
    for num in nums2:
      while i < len(nums1) and num >= nums1[i]:
        i += 1
      nums1.insert(i, num)
      i += 1
    print(nums1)
