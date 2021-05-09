Suppose an array of length `` n `` sorted in ascending order is __rotated__ between `` 1 `` and `` n `` times. For example, the array `` nums = [0,1,4,4,5,6,7] `` might become:

*   `` [4,5,6,7,0,1,4] `` if it was rotated `` 4 `` times.
*   `` [0,1,4,4,5,6,7] `` if it was rotated `` 7 `` times.

Notice that __rotating__ an array `` [a[0], a[1], a[2], ..., a[n-1]] `` 1 time results in the array `` [a[n-1], a[0], a[1], a[2], ..., a[n-2]] ``.

Given the sorted rotated array `` nums `` that may contain __duplicates__, return _the minimum element of this array_.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [1,3,5]
<strong>Output:</strong> 1
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [2,2,2,0,1]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   `` 1 &lt;= n &lt;= 5000 ``
*   `` -5000 &lt;= nums[i] &lt;= 5000 ``
*   `` nums `` is sorted and rotated between `` 1 `` and `` n `` times.

&nbsp;
__Follow up:__ This is the same as <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/" target="_blank">Find Minimum in Rotated Sorted Array</a> but with duplicates. Would allow duplicates affect the run-time complexity? How and why?