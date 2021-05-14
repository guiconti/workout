You are given an `` n x n `` `` grid `` where you have placed some `` 1 x 1 x 1 `` cubes. Each value `` v = grid[i][j] `` represents a tower of `` v `` cubes placed on top of cell `` (i, j) ``.

After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.

Return _the total surface area of the resulting shapes_.

__Note:__ The bottom face of each shape counts toward its surface area.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid1.jpg" style="width: 82px; height: 82px;"/>

<pre>
<strong>Input:</strong> grid = [[2]]
<strong>Output:</strong> 10
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid2.jpg" style="width: 162px; height: 162px;"/>

<pre>
<strong>Input:</strong> grid = [[1,2],[3,4]]
<strong>Output:</strong> 34
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid3.jpg" style="width: 162px; height: 162px;"/>

<pre>
<strong>Input:</strong> grid = [[1,0],[0,2]]
<strong>Output:</strong> 16
</pre>

__Example 4:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid4.jpg" style="width: 242px; height: 242px;"/>

<pre>
<strong>Input:</strong> grid = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> 32
</pre>

__Example 5:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid5.jpg" style="width: 242px; height: 242px;"/>

<pre>
<strong>Input:</strong> grid = [[2,2,2],[2,1,2],[2,2,2]]
<strong>Output:</strong> 46
</pre>

&nbsp;

__Constraints:__

*   `` n == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 &lt;= n &lt;= 50 ``
*   `` 0 &lt;= grid[i][j] &lt;= 50 ``