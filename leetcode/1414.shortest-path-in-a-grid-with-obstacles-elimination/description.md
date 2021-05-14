Given a `` m * n `` grid, where each cell is either `` 0 `` (empty)&nbsp;or `` 1 `` (obstacle).&nbsp;In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner&nbsp;`` (0, 0) ``&nbsp;to the lower right corner&nbsp;`` (m-1, n-1) `` given that you can eliminate&nbsp;__at most__ `` k `` obstacles. If it is not possible to find such&nbsp;walk return -1.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> 
grid = 
[[0,0,0],
&nbsp;[1,1,0],
 [0,0,0],
&nbsp;[0,1,1],
 [0,0,0]], 
k = 1
<strong>Output:</strong> 6
<strong>Explanation: 
</strong>The shortest path without eliminating any obstacle is 10.&nbsp;
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is <code>(0,0) -&gt; (0,1) -&gt; (0,2) -&gt; (1,2) -&gt; (2,2) -&gt; <strong>(3,2)</strong> -&gt; (4,2)</code>.
</pre>

&nbsp;

__Example 2:__

<pre>
<strong>Input:</strong> 
grid = 
[[0,1,1],
&nbsp;[1,1,1],
&nbsp;[1,0,0]], 
k = 1
<strong>Output:</strong> -1
<strong>Explanation: 
</strong>We need to eliminate at least two obstacles to find such a walk.
</pre>

&nbsp;

__Constraints:__

*   `` grid.length&nbsp;== m ``
*   `` grid[0].length&nbsp;== n ``
*   `` 1 &lt;= m, n &lt;= 40 ``
*   `` 1 &lt;= k &lt;= m*n ``
*   <code>grid[i][j] == 0 <strong>or</strong> 1</code>
*   `` grid[0][0] == grid[m-1][n-1] == 0 ``