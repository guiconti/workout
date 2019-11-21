/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
const findMedianSortedArrays = (nums1, nums2) => {
  if (nums1.length > nums2.length) {
    return findMedianSortedArrays(nums2, nums1);
  }
  let start = 0;
  let end = nums1.length;
  
  if (nums1.length === 0) {
    if (nums2.length % 2 === 0) {
      return (nums2[Math.floor(nums2.length / 2) - 1] + nums2[Math.floor(nums2.length / 2)]) / 2;
    }
    return nums2[Math.floor(nums2.length / 2)];
  }
  
  while (start <= end) {
    let partitionX = Math.floor((start + end) / 2);
    let partitionY = Math.floor((nums1.length + nums2.length + 1) / 2) - partitionX;
    
    let maxLeftX = partitionX === 0 ? Number.MIN_SAFE_INTEGER : nums1[partitionX - 1];
    let minRightX = partitionX >= nums1.length ? Number.MAX_SAFE_INTEGER : nums1[partitionX];
    let maxLeftY = partitionY === 0 ? Number.MIN_SAFE_INTEGER : nums2[partitionY - 1];
    let minRightY = partitionY >= nums2.length ? Number.MAX_SAFE_INTEGER : nums2[partitionY];
    
    console.log(partitionX, partitionY, maxLeftX, minRightX, maxLeftY, minRightY);
    
    if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
      if ((nums1.length + nums2.length) % 2 === 0) {
        return (Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2;
      } else {
        return Math.max(maxLeftX, maxLeftY);
      }
    } else if (maxLeftX > minRightY) {
      end = partitionX - 1;
    } else {
      start = partitionX + 1;
    }
  }
};