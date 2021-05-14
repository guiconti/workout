You are given an `` m x n `` binary matrix `` grid ``, where `` 0 `` represents a sea cell and `` 1 `` represents a land cell.

A __move__ consists of walking from one land cell to another adjacent (__4-directionally__) land cell or walking off the boundary of the `` grid ``.

Return _the number of land cells in_ `` grid `` _for which we cannot walk off the boundary of the grid in any number of __moves___.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/enclaves1.jpg" style="width: 333px; height: 333px;"/>

<pre>
<strong>Input:</strong> grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/enclaves2.jpg" style="width: 333px; height: 333px;"/>

<pre>
<strong>Input:</strong> grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> All 1s are either on the boundary or can reach the boundary.
</pre>

&nbsp;

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 &lt;= m, n &lt;= 500 ``
*   `` grid[i][j] `` is either `` 0 `` or `` 1 ``.