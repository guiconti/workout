Given a 2D&nbsp;`` grid `` consisting&nbsp;of `` 1 ``s (land)&nbsp;and `` 0 ``s (water).&nbsp; An _island_ is a maximal 4-directionally (horizontal or vertical) connected group of `` 1 ``s.

The grid is said to be __connected__ if we have __exactly one&nbsp;island__, otherwise is said __disconnected__.

In one day, we are allowed to change __any __single land cell `` (1) `` into a water cell `` (0) ``.

Return _the minimum number of days_ to disconnect the grid.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/08/13/1926_island.png" style="width: 498px; height: 139px;"/></strong>

<pre>
<strong>Input:</strong> grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> grid = [[1,1]]
<strong>Output:</strong> 2
<strong>Explanation: </strong>Grid of full water is also disconnected ([[1,1]] -&gt; [[0,0]]), 0 islands.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> grid = [[1,0,1,0]]
<strong>Output:</strong> 0
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> grid = [[1,1,0,1,1],
&nbsp;              [1,1,1,1,1],
&nbsp;              [1,1,0,1,1],
&nbsp;              [1,1,0,1,1]]
<strong>Output:</strong> 1
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> grid = [[1,1,0,1,1],
&nbsp;              [1,1,1,1,1],
&nbsp;              [1,1,0,1,1],
&nbsp;              [1,1,1,1,1]]
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= grid.length, grid[i].length &lt;= 30 ``
*   `` grid[i][j] ``&nbsp;is `` 0 `` or `` 1 ``.