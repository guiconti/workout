Given an `` m x n `` integers `` matrix ``, return _the length of the longest increasing path in _`` matrix ``.

From each cell, you can either move in four directions: left, right, up, or down. You __may not__ move __diagonally__ or move __outside the boundary__ (i.e., wrap-around is not allowed).

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg" style="width: 242px; height: 242px;"/>

<strong>Input:</strong> matrix = [[9,9,4],[6,6,8],[2,1,1]]
    <strong>Output:</strong> 4
    <strong>Explanation:</strong> The longest increasing path is [1, 2, 6, 9].

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg" style="width: 253px; height: 253px;"/>

<strong>Input:</strong> matrix = [[3,4,5],[3,2,6],[2,2,1]]
    <strong>Output:</strong> 4
    <strong>Explanation: </strong>The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

__Example 3:__

<pre>
<strong>Input:</strong> matrix = [[1]]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 &lt;= m, n &lt;= 200 ``
*   <code>0 &lt;= matrix[i][j] &lt;= 2<sup>31</sup> - 1</code>