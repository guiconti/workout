You are given a __0-indexed__ integer array `` nums `` and an integer `` k ``.

You are initially standing at index `` 0 ``. In one move, you can jump at most `` k `` steps forward without going outside the boundaries of the array. That is, you can jump from index `` i `` to any index in the range `` [i + 1, min(n - 1, i + k)] `` __inclusive__.

You want to reach the last index of the array (index `` n - 1 ``). Your __score__ is the __sum__ of all `` nums[j] `` for each index `` j `` you visited in the array.

Return _the __maximum score__ you can get_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [<u>1</u>,<u>-1</u>,-2,<u>4</u>,-7,<u>3</u>], k = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [<u>10</u>,-5,-2,<u>4</u>,0,<u>3</u>], k = 3
<strong>Output:</strong> 17
<strong>Explanation:</strong> You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   &nbsp;<code>1 &lt;= nums.length, k &lt;= 10<sup>5</sup></code>
*   <code>-10<sup>4</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup>4</sup></code>