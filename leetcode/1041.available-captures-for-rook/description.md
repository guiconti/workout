On an `` 8 x 8 `` chessboard, there is __exactly one__ white rook `` 'R' `` and some number of white bishops `` 'B' ``, black pawns `` 'p' ``, and empty squares `` '.' ``.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered __attacking__ a pawn if the rook can capture the pawn on the rook's turn. The __number of available captures__ for the white rook is the number of pawns that the rook is __attacking__.

Return _the __number of available captures__ for the white rook_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/02/20/1253_example_1_improved.PNG" style="width: 300px; height: 305px;"/>

<pre>
<strong>Input:</strong> board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> In this example, the rook is attacking all the pawns.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/02/19/1253_example_2_improved.PNG" style="width: 300px; height: 306px;"/>

<pre>
<strong>Input:</strong> board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The bishops are blocking the rook from attacking any of the pawns.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/02/20/1253_example_3_improved.PNG" style="width: 300px; height: 305px;"/>

<pre>
<strong>Input:</strong> board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The rook is attacking the pawns at positions b5, d6, and f5.
</pre>

&nbsp;

__Constraints:__

*   `` board.length == 8 ``
*   `` board[i].length == 8 ``
*   `` board[i][j] `` is either `` 'R' ``, `` '.' ``, `` 'B' ``, or `` 'p' ``
*   There is exactly one cell with `` board[i][j] == 'R' ``