Given an `` m x n `` binary matrix `` mat ``, return _the distance of the nearest _`` 0 ``_ for each cell_.

The distance between two adjacent cells is `` 1 ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg" style="width: 253px; height: 253px;"/>

<pre>
<strong>Input:</strong> mat = [[0,0,0],[0,1,0],[0,0,0]]
<strong>Output:</strong> [[0,0,0],[0,1,0],[0,0,0]]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg" style="width: 253px; height: 253px;"/>

<pre>
<strong>Input:</strong> mat = [[0,0,0],[0,1,0],[1,1,1]]
<strong>Output:</strong> [[0,0,0],[0,1,0],[1,2,1]]
</pre>

&nbsp;

__Constraints:__

*   `` m == mat.length ``
*   `` n == mat[i].length ``
*   <code>1 &lt;= m, n &lt;= 10<sup>4</sup></code>
*   <code>1 &lt;= m * n &lt;= 10<sup>4</sup></code>
*   `` mat[i][j] `` is either `` 0 `` or `` 1 ``.
*   There is at least one `` 0 `` in `` mat ``.