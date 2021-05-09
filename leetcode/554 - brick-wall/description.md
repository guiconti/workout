There is a rectangular brick wall in front of you with `` n `` rows of bricks. The <code>i<sup>th</sup></code> row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array `` wall `` that contains the information about the wall, return _the minimum number of crossed bricks after drawing such a vertical line_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/cutwall-grid.jpg" style="width: 493px; height: 577px;"/>

<pre>
<strong>Input:</strong> wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
<strong>Output:</strong> 2
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> wall = [[1],[1],[1]]
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   `` n == wall.length ``
*   <code>1 &lt;= n &lt;= 10<sup>4</sup></code>
*   <code>1 &lt;= wall[i].length &lt;= 10<sup>4</sup></code>
*   <code>1 &lt;= sum(wall[i].length) &lt;= 2 * 10<sup>4</sup></code>
*   `` sum(wall[i]) `` is the same for each row `` i ``.
*   <code>1 &lt;= wall[i][j] &lt;= 2<sup>31</sup> - 1</code>