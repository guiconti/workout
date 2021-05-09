Given an `` m x n `` matrix `` board `` where each cell is a battleship `` 'X' `` or empty `` '.' ``, return _the number of the __battleships__ on_ `` board ``.

__Battleships__ can only be placed horizontally or vertically on `` board ``. In other words, they can only be made of the shape `` 1 x k `` (`` 1 `` row, `` k `` columns) or `` k x 1 `` (`` k `` rows, `` 1 `` column), where `` k `` can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/10/battelship-grid.jpg" style="width: 333px; height: 333px;"/>

<pre>
<strong>Input:</strong> board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
<strong>Output:</strong> 2
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> board = [["."]]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` m == board.length ``
*   `` n == board[i].length ``
*   `` 1 &lt;= m, n &lt;= 200 ``
*   `` board[i][j] `` is either `` '.' `` or `` 'X' ``.

&nbsp;

__Follow up:__ Could you do it in one-pass, using only `` O(1) `` extra memory and without modifying the values `` board ``?