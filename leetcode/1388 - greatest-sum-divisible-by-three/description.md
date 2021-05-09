Given an array&nbsp;`` nums ``&nbsp;of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,6,5,1,8]
<strong>Output:</strong> 18
<strong>Explanation:</strong> Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [4]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since 4 is not divisible by 3, do not pick any number.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4,4]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 4 * 10^4 ``
*   `` 1 &lt;= nums[i] &lt;= 10^4 ``