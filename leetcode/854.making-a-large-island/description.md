You are given an `` n x n `` binary matrix `` grid ``. You are allowed to change __at most one__ `` 0 `` to be `` 1 ``.

Return _the size of the largest __island__ in_ `` grid `` _after applying this operation_.

An __island__ is a 4-directionally connected group of `` 1 ``s.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> grid = [[1,0],[0,1]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> grid = [[1,1],[1,0]]
<strong>Output:</strong> 4
<strong>Explanation: </strong>Change the 0 to 1 and make the island bigger, only one island with area = 4.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> grid = [[1,1],[1,1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Can't change any 0 to 1, only one island with area = 4.
</pre>

&nbsp;

__Constraints:__

*   `` n == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 &lt;= n &lt;= 500 ``
*   `` grid[i][j] `` is either `` 0 `` or `` 1 ``.