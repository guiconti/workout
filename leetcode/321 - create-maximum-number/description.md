You are given two integer arrays `` nums1 `` and `` nums2 `` of lengths `` m `` and `` n `` respectively. `` nums1 `` and `` nums2 `` represent the digits of two numbers. You are also given an integer `` k ``.

Create the maximum number of length `` k &lt;= m + n `` from digits of the two numbers. The relative order of the digits from the same array must be preserved.

Return an array of the `` k `` digits representing the answer.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
<strong>Output:</strong> [9,8,6,5,3]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums1 = [6,7], nums2 = [6,0,4], k = 5
<strong>Output:</strong> [6,7,6,0,4]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums1 = [3,9], nums2 = [8,9], k = 3
<strong>Output:</strong> [9,8,9]
</pre>

&nbsp;

__Constraints:__

*   `` m == nums1.length ``
*   `` n == nums2.length ``
*   `` 1 &lt;= m, n &lt;= 500 ``
*   `` 0 &lt;= nums1[i], nums2[i] &lt;= 9 ``
*   `` 1 &lt;= k &lt;= m + n ``

&nbsp;

__Follow up:__ Try to optimize your time and space complexity.