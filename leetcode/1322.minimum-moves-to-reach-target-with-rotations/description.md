In an&nbsp;`` n*n ``&nbsp;grid, there is a snake that spans 2 cells and starts moving from the top left corner at `` (0, 0) `` and `` (0, 1) ``. The grid has empty cells represented by zeros and blocked cells represented by ones. The snake wants to reach the lower right corner at&nbsp;`` (n-1, n-2) ``&nbsp;and&nbsp;`` (n-1, n-1) ``.

In one move the snake can:

<ul><li>Move one cell to the right&nbsp;if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.</li><li>Move down one cell&nbsp;if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.</li><li>Rotate clockwise if it's in a horizontal position and the two cells under it are both empty. In that case the snake moves from&nbsp;<code>(r, c)</code>&nbsp;and&nbsp;<code>(r, c+1)</code>&nbsp;to&nbsp;<code>(r, c)</code>&nbsp;and&nbsp;<code>(r+1, c)</code>.<br/>
<img alt="" src="https://assets.leetcode.com/uploads/2019/09/24/image-2.png" style="width: 300px; height: 134px;"/></li><li>Rotate counterclockwise&nbsp;if it's in a vertical position and the two cells to its right are both empty. In that case the snake moves from&nbsp;<code>(r, c)</code>&nbsp;and&nbsp;<code>(r+1, c)</code>&nbsp;to&nbsp;<code>(r, c)</code>&nbsp;and&nbsp;<code>(r, c+1)</code>.<br/>
<img alt="" src="https://assets.leetcode.com/uploads/2019/09/24/image-1.png" style="width: 300px; height: 121px;"/></li></ul>

Return the minimum number of moves to reach the target.

If there is no way to reach the target, return&nbsp;`` -1 ``.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/24/image.png" style="width: 400px; height: 439px;"/></strong>

<pre>
<strong>Input:</strong> grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
&nbsp;              [0,0,0,0,1,1],
&nbsp;              [0,0,1,0,1,0],
&nbsp;              [0,1,1,0,0,0],
&nbsp;              [0,1,1,0,0,0]]
<strong>Output:</strong> 11
<strong>Explanation:
</strong>One possible solution is [right, right, rotate clockwise, right, down, down, down, down, rotate counterclockwise, right, down].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> grid = [[0,0,1,1,1,1],
&nbsp;              [0,0,0,0,1,1],
&nbsp;              [1,1,0,0,0,1],
&nbsp;              [1,1,1,0,0,1],
&nbsp;              [1,1,1,0,0,1],
&nbsp;              [1,1,1,0,0,0]]
<strong>Output:</strong> 9
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= n &lt;= 100 ``
*   `` 0 &lt;= grid[i][j] &lt;= 1 ``
*   It is guaranteed that the snake starts at empty cells.