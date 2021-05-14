You are given an integer array `` nums `` and an integer `` x ``. In one operation, you can either remove the leftmost or the rightmost element from the array `` nums `` and subtract its value from `` x ``. Note that this __modifies__ the array for future operations.

Return _the __minimum number__ of operations to reduce _`` x `` _to __exactly___ `` 0 `` _if it's possible__, otherwise, return _`` -1 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,1,4,2,3], x = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> The optimal solution is to remove the last two elements to reduce x to zero.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [5,6,7,8,9], x = 4
<strong>Output:</strong> -1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [3,2,20,1,1,3], x = 10
<strong>Output:</strong> 5
<strong>Explanation:</strong> The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code>
*   <code>1 &lt;= x &lt;= 10<sup>9</sup></code>