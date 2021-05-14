Given an integer array `` nums `` and an integer `` k ``, return the maximum sum of a __non-empty__ subsequence of that array such that for every two __consecutive__ integers in the subsequence, `` nums[i] `` and `` nums[j] ``, where `` i &lt; j ``, the condition `` j - i &lt;= k `` is satisfied.

A _subsequence_ of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [10,2,-10,5,20], k = 2
<strong>Output:</strong> 37
<b>Explanation:</b> The subsequence is [10, 2, 5, 20].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [-1,-2,-3], k = 1
<strong>Output:</strong> -1
<b>Explanation:</b> The subsequence must be non-empty, so we choose the largest number.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [10,-2,-10,-5,20], k = 2
<strong>Output:</strong> 23
<b>Explanation:</b> The subsequence is [10, -2, -5, 20].
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>