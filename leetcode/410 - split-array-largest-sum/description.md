Given an array `` nums `` which consists of non-negative integers and an integer `` m ``, you can split the array into `` m `` non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these `` m `` subarrays.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [7,2,5,10,8], m = 2
<strong>Output:</strong> 18
<strong>Explanation:</strong>
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5], m = 2
<strong>Output:</strong> 9
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,4,4], m = 3
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 1000 ``
*   <code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code>
*   `` 1 &lt;= m &lt;= min(50, nums.length) ``