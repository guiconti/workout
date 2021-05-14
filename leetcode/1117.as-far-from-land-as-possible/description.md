Given an `` n x n `` `` grid ``&nbsp;containing only values `` 0 `` and `` 1 ``, where&nbsp;`` 0 `` represents water&nbsp;and `` 1 `` represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance.&nbsp;If no land or water exists in the grid, return `` -1 ``.

The distance used in this problem is the Manhattan distance:&nbsp;the distance between two cells `` (x0, y0) `` and `` (x1, y1) `` is `` |x0 - x1| + |y0 - y1| ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/05/03/1336_ex1.JPG" style="width: 185px; height: 87px;"/>

<pre>
<strong>Input:</strong> grid = [[1,0,1],[0,0,0],[1,0,1]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The cell (1, 1) is as far as possible from all the land with distance 2.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/05/03/1336_ex2.JPG" style="width: 184px; height: 87px;"/>

<pre>
<strong>Input:</strong> grid = [[1,0,0],[0,0,0],[0,0,0]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The cell (2, 2) is as far as possible from all the land with distance 4.
</pre>

&nbsp;

__Constraints:__

*   `` n == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 &lt;= n&nbsp;&lt;= 100 ``
*   `` grid[i][j] ``&nbsp;is `` 0 `` or `` 1 ``