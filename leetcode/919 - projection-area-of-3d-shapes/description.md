You are given an `` n x n `` `` grid `` where we place some `` 1 x 1 x 1 `` cubes that are axis-aligned with the `` x ``, `` y ``, and `` z `` axes.

Each value `` v = grid[i][j] `` represents a tower of `` v `` cubes placed on top of the cell `` (i, j) ``.

We view the projection of these cubes onto the `` xy ``, `` yz ``, and `` zx `` planes.

A __projection__ is like a shadow, that maps our __3-dimensional__ figure to a __2-dimensional__ plane. We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return _the total area of all three projections_.

&nbsp;

__Example 1:__

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/02/shadow.png" style="width: 800px; height: 214px;"/>

<pre>
<strong>Input:</strong> grid = [[1,2],[3,4]]
<strong>Output:</strong> 17
<strong>Explanation:</strong> Here are the three projections ("shadows") of the shape made with each axis-aligned plane.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> grid = [[2]]
<strong>Output:</strong> 5
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> grid = [[1,0],[0,2]]
<strong>Output:</strong> 8
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> grid = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> 14
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> grid = [[2,2,2],[2,1,2],[2,2,2]]
<strong>Output:</strong> 21
</pre>

&nbsp;

__Constraints:__

*   `` n == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 &lt;= n&nbsp;&lt;= 50 ``
*   `` 0 &lt;= grid[i][j] &lt;= 50 ``