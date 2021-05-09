Given an `` m x n `` matrix `` board `` containing `` 'X' `` and `` 'O' ``, _capture all regions surrounded by_ `` 'X' ``.

A region is __captured__ by flipping all `` 'O' ``s into `` 'X' ``s in that surrounded region.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg" style="width: 550px; height: 237px;"/>

<pre>
<strong>Input:</strong> board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
<strong>Output:</strong> [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
<strong>Explanation:</strong> Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> board = [["X"]]
<strong>Output:</strong> [["X"]]
</pre>

&nbsp;

__Constraints:__

*   `` m == board.length ``
*   `` n == board[i].length ``
*   `` 1 &lt;= m, n &lt;= 200 ``
*   `` board[i][j] `` is `` 'X' `` or `` 'O' ``.