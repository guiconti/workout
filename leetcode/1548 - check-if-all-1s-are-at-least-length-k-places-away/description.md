Given an array `` nums `` of 0s and 1s and an integer `` k ``, return `` True `` if all 1's are at least `` k `` places away from each other, otherwise return `` False ``.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png" style="width: 214px; height: 90px;"/></strong>

<pre>
<strong>Input:</strong> nums = [1,0,0,0,1,0,0,1], k = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> Each of the 1s are at least 2 places away from each other.
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png" style="width: 160px; height: 86px;"/></strong>

<pre>
<strong>Input:</strong> nums = [1,0,0,1,0,1], k = 2
<strong>Output:</strong> false
<strong>Explanation: </strong>The second 1 and third 1 are only one apart from each other.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1], k = 0
<strong>Output:</strong> true
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [0,1,0,1], k = 1
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   `` 0 &lt;= k &lt;= nums.length ``
*   `` nums[i] `` is `` 0 `` or `` 1 ``