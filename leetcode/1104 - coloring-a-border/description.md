Given a 2-dimensional&nbsp;`` grid `` of integers, each value in the grid represents the color of the grid square at that location.

Two squares belong to the same _connected component_ if and only if they have the same color and are next to each other in any of the 4 directions.

The&nbsp;_border_ of a connected component is&nbsp;all the squares in the connected component that are&nbsp;either 4-directionally adjacent to&nbsp;a square not in the component, or on the boundary of the grid (the first or last row or column).

Given a square at location&nbsp;`` (r0, c0) ``&nbsp;in the grid and a `` color ``, color the&nbsp;border of the connected component of that square with the given `` color ``, and return the final `` grid ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>grid = <span id="example-input-1-1">[[1,1],[1,2]]</span>, r0 = <span id="example-input-1-2">0</span>, c0 = <span id="example-input-1-3">0</span>, color = <span id="example-input-1-4">3</span>
<strong>Output: </strong><span id="example-output-1">[[3, 3], [3, 2]]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>grid = <span id="example-input-2-1">[[1,2,2],[2,3,2]]</span>, r0 = <span id="example-input-2-2">0</span>, c0 = <span id="example-input-2-3">1</span>, color = <span id="example-input-2-4">3</span>
<strong>Output: </strong><span id="example-output-2">[[1, 3, 3], [2, 3, 3]]</span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong>grid = <span id="example-input-3-1">[[1,1,1],[1,1,1],[1,1,1]]</span>, r0 = <span id="example-input-3-2">1</span>, c0 = <span id="example-input-3-3">1</span>, color = <span id="example-input-3-4">2</span>
<strong>Output: </strong><span id="example-output-3">[[2, 2, 2], [2, 1, 2], [2, 2, 2]]</span></pre>
</div>
</div>

&nbsp;

__Note:__

1.   `` 1 &lt;= grid.length &lt;= 50 ``
2.   `` 1 &lt;= grid[0].length &lt;= 50 ``
3.   `` 1 &lt;= grid[i][j] &lt;= 1000 ``
4.   `` 0 &lt;= r0 &lt; grid.length ``
5.   `` 0 &lt;= c0 &lt; grid[0].length ``
6.   `` 1 &lt;= color &lt;= 1000 ``