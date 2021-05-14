A `` 3 x 3 `` magic square is a `` 3 x 3 `` grid filled with distinct numbers __from __`` 1 ``__ to __`` 9 `` such that each row, column, and both diagonals all have the same sum.

Given a `` row x col ``&nbsp;`` grid ``&nbsp;of integers, how many `` 3 x 3 `` "magic square" subgrids are there?&nbsp; (Each subgrid is contiguous).

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/11/magic_main.jpg" style="width: 322px; height: 242px;"/>

<pre>
<strong>Input:</strong> grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
<strong>Output:</strong> 1
<strong>Explanation: </strong>
The following subgrid is a 3 x 3 magic square:
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/11/magic_valid.jpg" style="width: 242px; height: 242px;"/>
while this one is not:
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/11/magic_invalid.jpg" style="width: 242px; height: 242px;"/>
In total, there is only one magic square inside the given grid.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> grid = [[8]]
<strong>Output:</strong> 0
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> grid = [[4,4],[3,3]]
<strong>Output:</strong> 0
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> grid = [[4,7,8],[9,5,1],[2,3,6]]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` row == grid.length ``
*   `` col == grid[i].length ``
*   `` 1 &lt;= row, col &lt;= 10 ``
*   `` 0 &lt;= grid[i][j] &lt;= 15 ``