On an N x N `` board ``, the numbers from `` 1 `` to `` N*N `` are written&nbsp;_boustrophedonically_&nbsp;__starting from the bottom&nbsp;left of the board__, and alternating direction each row.&nbsp; For example, for a 6 x 6 board, the numbers are written as follows:

<pre>
<img alt="" src="https://assets.leetcode.com/uploads/2018/09/23/snakes.png" style="width: 254px; height: 200px;"/>
</pre>

You start on square `` 1 `` of the board (which is always in the last row and&nbsp;first column).&nbsp; Each move, starting from square `` x ``, consists of the following:

*   You choose a destination square `` S `` with number&nbsp;`` x+1 ``, `` x+2 ``, `` x+3 ``, `` x+4 ``, `` x+5 ``, or `` x+6 ``, provided this&nbsp;number is&nbsp;`` &lt;=&nbsp;N*N ``.	
    
    *   (This choice simulates the result of a standard 6-sided die roll: ie., there are always __at most 6 destinations, regardless of the size of the board__.)
    
    
    
*   If `` S ``&nbsp;has a snake or ladder, you move to the destination of that snake or ladder.&nbsp; Otherwise, you move to `` S ``.

A board square on row `` r `` and column `` c ``&nbsp;has a "snake or ladder" if `` board[r][c] != -1 ``.&nbsp; The destination of that snake or ladder is `` board[r][c] ``.

Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another&nbsp;snake or ladder, you do __not__ continue moving.&nbsp; (For example, if the board is \`\[\[4,-1\],\[-1,3\]\]\`, and on the first move your destination square is \`2\`, then you finish your first move at&nbsp;\`3\`, because you do __not__ continue moving to \`4\`.)

Return the least number of moves required to reach square 

<font face="monospace">N*N</font>

.&nbsp; If it is not possible, return `` -1 ``.

__Example 1:__

<pre>
<strong>Input: </strong>[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
<strong>Output: </strong>4
<strong>Explanation: </strong>
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
</pre>

__Note:__

1.   `` 2 &lt;= board.length = board[0].length&nbsp;&lt;= 20 ``
2.   `` board[i][j] ``&nbsp;is between `` 1 `` and `` N*N `` or is equal to `` -1 ``.
3.   The board&nbsp;square with number `` 1 `` has no snake or ladder.
4.   The board square with number `` N*N `` has no snake or ladder.