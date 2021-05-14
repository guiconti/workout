You are given `` n `` balloons, indexed from `` 0 `` to `` n - 1 ``. Each balloon is painted with a number on it represented by an array `` nums ``. You are asked to burst all the balloons.

If you burst the <code>i<sup>th</sup></code> balloon, you will get `` nums[i - 1] * nums[i] * nums[i + 1] `` coins. If `` i - 1 `` or `` i + 1 `` goes out of bounds of the array, then treat it as if there is a balloon with a `` 1 `` painted on it.

Return _the maximum coins you can collect by bursting the balloons wisely_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,1,5,8]
<strong>Output:</strong> 167
<strong>Explanation:</strong>
nums = [3,1,5,8] --&gt; [3,5,8] --&gt; [3,8] --&gt; [8] --&gt; []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,5]
<strong>Output:</strong> 10
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   `` 1 &lt;= n &lt;= 500 ``
*   `` 0 &lt;= nums[i] &lt;= 100 ``