Given an integer array `` nums `` and an integer `` k ``, find three non-overlapping subarrays of length `` k `` with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (__0-indexed__). If there are multiple answers, return the lexicographically smallest one.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,1,2,6,7,5,1], k = 2
<strong>Output:</strong> [0,3,5]
<strong>Explanation:</strong> Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,1,2,1,2,1,2,1], k = 2
<strong>Output:</strong> [0,2,4]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code>
*   <code>1 &lt;= nums[i] &lt;&nbsp;2<sup>16</sup></code>
*   `` 1 &lt;= k &lt;= floor(nums.length / 3) ``