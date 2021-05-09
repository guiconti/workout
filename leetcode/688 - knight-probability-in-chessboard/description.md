On an `` n x n `` chessboard, a knight starts at the cell `` (row, column) `` and attempts to make exactly `` k `` moves. The rows and columns are __0-indexed__, so the top-left cell is `` (0, 0) ``, and the bottom-right cell is `` (n - 1, n - 1) ``.

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

<img src="https://assets.leetcode.com/uploads/2018/10/12/knight.png" style="width: 300px; height: 300px;"/>

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly `` k `` moves or has moved off the chessboard.

Return _the probability that the knight remains on the board after it has stopped moving_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 3, k = 2, row = 0, column = 0
<strong>Output:</strong> 0.06250
<strong>Explanation:</strong> There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 1, k = 0, row = 0, column = 0
<strong>Output:</strong> 1.00000
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 25 ``
*   `` 0 &lt;= k &lt;= 100 ``
*   `` 0 &lt;= row, column &lt;= n ``