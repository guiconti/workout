Given an array of non-negative integers `` nums ``, you are initially positioned at the __first index__ of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> true
<strong>Explanation:</strong> Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [3,2,1,0,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code>
*   <code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code>