Given an `` n&nbsp;x n ``&nbsp;binary `` grid ``, in one step you can choose two __adjacent rows__ of the grid and swap them.

A grid is said to be __valid__ if all the cells above the main diagonal are __zeros__.

Return _the minimum number of steps_ needed to make the grid valid, or __-1__ if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell `` (1, 1) `` and ends at cell `` (n, n) ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/28/fw.jpg" style="width: 750px; height: 141px;"/>

<pre>
<strong>Input:</strong> grid = [[0,0,1],[1,1,0],[1,0,0]]
<strong>Output:</strong> 3
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/16/e2.jpg" style="width: 270px; height: 270px;"/>

<pre>
<strong>Input:</strong> grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> All rows are similar, swaps have no effect on the grid.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/16/e3.jpg" style="width: 200px; height: 200px;"/>

<pre>
<strong>Input:</strong> grid = [[1,0,0],[1,1,0],[1,1,1]]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` n == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 &lt;= n&nbsp;&lt;= 200 ``
*   `` grid[i][j] `` is `` 0 `` or `` 1 ``