You are given an `` m x n `` integer matrix `` heights `` representing the height of each unit cell in a continent. The __Pacific ocean__ touches the continent's left and top edges, and the A__tlantic ocean__ touches the continent's right and bottom edges.

Water can only flow in four directions: up, down, left, and right. Water flows from a cell to an adjacent one with an equal or lower height.

Return _a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/26/ocean-grid.jpg" style="width: 573px; height: 573px;"/>

<pre>
<strong>Input:</strong> heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
<strong>Output:</strong> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> heights = [[2,1],[1,2]]
<strong>Output:</strong> [[0,0],[0,1],[1,0],[1,1]]
</pre>

&nbsp;

__Constraints:__

*   `` m == heights.length ``
*   `` n == heights[i].length ``
*   `` 1 &lt;= m, n &lt;= 200 ``
*   <code>1 &lt;= heights[i][j] &lt;= 10<sup>5</sup></code>