Given an array of integers `` nums `` which is sorted in ascending order, and an integer `` target ``, write a function to search `` target `` in `` nums ``. If `` target `` exists, then return its index. Otherwise, return `` -1 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [-1,0,3,5,9,12], target = 9
<strong>Output:</strong> 4
<strong>Explanation:</strong> 9 exists in nums and its index is 4
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [-1,0,3,5,9,12], target = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> 2 does not exist in nums so return -1
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   `` -9999 &lt;= nums[i], target &lt;= 9999 ``
*   All the integers in `` nums `` are __unique__.
*   `` nums `` is sorted in an ascending order.