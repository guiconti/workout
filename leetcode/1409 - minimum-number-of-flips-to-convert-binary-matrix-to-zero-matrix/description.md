Given a `` m x n `` binary matrix `` mat ``. In one step, you can choose one cell and flip it and all the four neighbors of it if they exist (Flip is changing `` 1 `` to `` 0 `` and `` 0 `` to `` 1 ``). A pair of cells are called neighbors if they share one edge.

Return the _minimum number of steps_ required to convert `` mat `` to a zero matrix or `` -1 `` if you cannot.

A __binary matrix__ is a matrix with all cells equal to `` 0 `` or `` 1 `` only.

A __zero matrix__ is a matrix with all cells equal to `` 0 ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/28/matrix.png" style="width: 409px; height: 86px;"/>

<pre>
<strong>Input:</strong> mat = [[0,0],[0,1]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> mat = [[0]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Given matrix is a zero matrix. We don't need to change it.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> mat = [[1,1,1],[1,0,1],[0,0,0]]
<strong>Output:</strong> 6
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> mat = [[1,0,0],[1,0,0]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> Given matrix can't be a zero matrix
</pre>

&nbsp;

__Constraints:__

*   `` m == mat.length ``
*   `` n == mat[i].length ``
*   `` 1 &lt;= m, n &lt;= 3 ``
*   `` mat[i][j] `` is either `` 0 `` or `` 1 ``.