An integer array is called arithmetic if it consists of __at least three elements__ and if the difference between any two consecutive elements is the same.

*   For example, `` [1,3,5,7,9] ``, `` [7,7,7,7] ``, and `` [3,-1,-5,-9] `` are arithmetic sequences.

Given an integer array `` nums ``, return _the number of arithmetic __subarrays__ of_ `` nums ``.

A __subarray__ is a contiguous subsequence of the array.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 5000 ``
*   `` -1000 &lt;= nums[i] &lt;= 1000 ``