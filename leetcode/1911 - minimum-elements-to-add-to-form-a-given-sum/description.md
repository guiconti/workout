You are given an integer array `` nums `` and two integers `` limit `` and `` goal ``. The array `` nums `` has an interesting property that `` abs(nums[i]) &lt;= limit ``.

Return _the minimum number of elements you need to add to make the sum of the array equal to _`` goal ``. The array must maintain its property that `` abs(nums[i]) &lt;= limit ``.

Note that `` abs(x) `` equals `` x `` if `` x &gt;= 0 ``, and `` -x `` otherwise.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,-1,1], limit = 3, goal = -4
<strong>Output:</strong> 2
<strong>Explanation:</strong> You can add -2 and -3, then the sum of the array will be 1 - 1 + 1 - 2 - 3 = -4.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,-10,9,1], limit = 100, goal = 0
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= limit &lt;= 10<sup>6</sup></code>
*   `` -limit &lt;= nums[i] &lt;= limit ``
*   <code>-10<sup>9</sup> &lt;= goal &lt;= 10<sup>9</sup></code>