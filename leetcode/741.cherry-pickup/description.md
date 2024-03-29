You are given an `` n x n `` `` grid `` representing a field of cherries, each cell is one of three possible integers.

*   `` 0 `` means the cell is empty, so you can pass through,
*   `` 1 `` means the cell contains a cherry that you can pick up and pass through, or
*   `` -1 `` means the cell contains a thorn that blocks your way.

Return _the maximum number of cherries you can collect by following the rules below_:

*   Starting at the position `` (0, 0) `` and reaching `` (n - 1, n - 1) `` by moving right or down through valid path cells (cells with value `` 0 `` or `` 1 ``).
*   After reaching `` (n - 1, n - 1) ``, returning to `` (0, 0) `` by moving left or up through valid path cells.
*   When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell `` 0 ``.
*   If there is no valid path between `` (0, 0) `` and `` (n - 1, n - 1) ``, then no cherries can be collected.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/14/grid.jpg" style="width: 242px; height: 242px;"/>

<pre>
<strong>Input:</strong> grid = [[0,1,-1],[1,0,-1],[1,1,1]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` n == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 &lt;= n &lt;= 50 ``
*   `` grid[i][j] `` is `` -1 ``, `` 0 ``, or `` 1 ``.
*   `` grid[0][0] != -1 ``
*   `` grid[n - 1][n - 1] != -1 ``