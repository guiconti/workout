You are given an `` m x n `` binary matrix `` grid ``. An island is a group of `` 1 ``'s (representing land) connected __4-directionally__ (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The __area__ of an island is the number of cells with a value `` 1 `` in the island.

Return _the maximum __area__ of an island in _`` grid ``. If there is no island, return `` 0 ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg" style="width: 500px; height: 310px;"/>

<pre>
<strong>Input:</strong> grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The answer is not 11, because the island must be connected 4-directionally.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> grid = [[0,0,0,0,0,0,0,0]]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 &lt;= m, n &lt;= 50 ``
*   `` grid[i][j] `` is either `` 0 `` or `` 1 ``.