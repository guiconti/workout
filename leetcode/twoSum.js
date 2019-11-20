/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (nums, target) => {
  hashMap = {};
  for (let i = 0; i < nums.length; i++) {
    const numToBeFound = target - nums[i];
    if (hashMap[numToBeFound] !== undefined && hashMap[numToBeFound] !== i) {
      return [i, hashMap[numToBeFound]];
    }
    hashMap[nums[i]] = i;
  }
};