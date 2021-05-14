A robot is located at the top-left corner of a `` m x n `` grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

&nbsp;

__Example 1:__

<img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" style="width: 400px; height: 183px;"/>

<pre>
<strong>Input:</strong> m = 3, n = 7
<strong>Output:</strong> 28
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> m = 3, n = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong>
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right
3. Down -&gt; Right -&gt; Down
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> m = 7, n = 3
<strong>Output:</strong> 28
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> m = 3, n = 3
<strong>Output:</strong> 6
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= m, n &lt;= 100 ``
*   It's guaranteed that the answer will be less than or equal to <code>2 * 10<sup>9</sup></code>.