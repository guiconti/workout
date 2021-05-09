You are given `` row x col `` `` grid `` representing a map where `` grid[i][j] = 1 `` represents&nbsp;land and `` grid[i][j] = 0 `` represents water.

Grid cells are connected __horizontally/vertically__ (not diagonally). The `` grid `` is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

&nbsp;

__Example 1:__

<img src="https://assets.leetcode.com/uploads/2018/10/12/island.png" style="width: 221px; height: 213px;"/>

<pre>
<strong>Input:</strong> grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
<strong>Output:</strong> 16
<strong>Explanation:</strong> The perimeter is the 16 yellow stripes in the image above.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> grid = [[1]]
<strong>Output:</strong> 4
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> grid = [[1,0]]
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` row == grid.length ``
*   `` col == grid[i].length ``
*   `` 1 &lt;= row, col &lt;= 100 ``
*   `` grid[i][j] `` is `` 0 `` or `` 1 ``.