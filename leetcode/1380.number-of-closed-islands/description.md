Given a 2D&nbsp;`` grid `` consists of `` 0s `` (land)&nbsp;and `` 1s `` (water).&nbsp; An _island_ is a maximal 4-directionally connected group of <code><font face="monospace">0</font>s</code> and a _closed island_&nbsp;is an island __totally__&nbsp;(all left, top, right, bottom) surrounded by `` 1s. ``

Return the number of _closed islands_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png" style="width: 240px; height: 120px;"/>

<pre>
<strong>Input:</strong> grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
Islands in gray are closed because they are completely surrounded by water (group of 1s).</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/10/31/sample_4_1610.png" style="width: 160px; height: 80px;"/>

<pre>
<strong>Input:</strong> grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> grid = [[1,1,1,1,1,1,1],
&nbsp;              [1,0,0,0,0,0,1],
&nbsp;              [1,0,1,1,1,0,1],
&nbsp;              [1,0,1,0,1,0,1],
&nbsp;              [1,0,1,1,1,0,1],
&nbsp;              [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= grid.length, grid[0].length &lt;= 100 ``
*   `` 0 &lt;= grid[i][j] &lt;=1 ``