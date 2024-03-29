Given an array of non-negative integers `` nums ``, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [2,3,0,1,4]
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 1000 ``
*   <code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code>