Given an array of integers `` nums `` and an integer `` k ``. A continuous subarray is called __nice__ if there are `` k `` odd numbers on it.

Return _the number of __nice__ sub-arrays_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,1,2,1,1], k = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [2,4,6], k = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no odd numbers in the array.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [2,2,2,1,2,2,1,2,2,2], k = 2
<strong>Output:</strong> 16
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 50000 ``
*   `` 1 &lt;= nums[i] &lt;= 10^5 ``
*   `` 1 &lt;= k &lt;= nums.length ``