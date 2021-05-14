You have `` n `` coins and you want to build a staircase with these coins. The staircase consists of `` k `` rows where the <code>i<sup>th</sup></code> row has exactly `` i `` coins. The last row of the staircase __may be__ incomplete.

Given the integer `` n ``, return _the number of __complete rows__ of the staircase you will build_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/arrangecoins1-grid.jpg" style="width: 253px; height: 253px;"/>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> Because the 3<sup>rd</sup> row is incomplete, we return 2.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/arrangecoins2-grid.jpg" style="width: 333px; height: 333px;"/>

<pre>
<strong>Input:</strong> n = 8
<strong>Output:</strong> 3
<strong>Explanation:</strong> Because the 4<sup>th</sup> row is incomplete, we return 3.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code>