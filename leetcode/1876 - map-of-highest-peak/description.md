You are given an integer matrix `` isWater `` of size `` m x n `` that represents a map of __land__ and __water__ cells.

*   If `` isWater[i][j] == 0 ``, cell `` (i, j) `` is a __land__ cell.
*   If `` isWater[i][j] == 1 ``, cell `` (i, j) `` is a __water__ cell.

You must assign each cell a height in a way that follows these rules:

*   The height of each cell must be non-negative.
*   If the cell is a __water__ cell, its height must be `` 0 ``.
*   Any two adjacent cells must have an absolute height difference of __at most__ `` 1 ``. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

Find an assignment of heights such that the maximum height in the matrix is __maximized__.

Return _an integer matrix _`` height ``_ of size _`` m x n ``_ where _`` height[i][j] ``_ is cell _`` (i, j) ``_'s height. If there are multiple solutions, return __any__ of them_.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-82045-am.png" style="width: 220px; height: 219px;"/></strong>

<pre>
<strong>Input:</strong> isWater = [[0,1],[0,0]]
<strong>Output:</strong> [[1,0],[2,1]]
<strong>Explanation:</strong> The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-82050-am.png" style="width: 300px; height: 296px;"/></strong>

<pre>
<strong>Input:</strong> isWater = [[0,0,1],[1,0,0],[0,0,0]]
<strong>Output:</strong> [[1,1,0],[0,1,1],[1,2,2]]
<strong>Explanation:</strong> A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.
</pre>

&nbsp;

__Constraints:__

*   `` m == isWater.length ``
*   `` n == isWater[i].length ``
*   `` 1 &lt;= m, n &lt;= 1000 ``
*   `` isWater[i][j] `` is `` 0 `` or `` 1 ``.
*   There is at least __one__ water cell.