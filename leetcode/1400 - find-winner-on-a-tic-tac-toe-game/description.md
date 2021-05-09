Tic-tac-toe is played&nbsp;by&nbsp;two players _A_ and _B_ on a&nbsp;_3_&nbsp;x&nbsp;_3_&nbsp;grid.

Here are the rules of Tic-Tac-Toe:

*   Players take turns placing characters into empty squares (" ").
*   The first player _A_ always places "X" characters, while the second player _B_&nbsp;always places "O" characters.
*   "X" and "O" characters are always placed into empty squares, never on filled ones.
*   The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
*   The game also ends if all squares are non-empty.
*   No more moves can be played if the game is over.

Given an array `` moves `` where each element&nbsp;is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which _A_ and _B_ play.

Return the winner of the game if it exists (_A_ or _B_), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that&nbsp;`` moves `` is&nbsp;__valid__ (It follows the rules of Tic-Tac-Toe),&nbsp;the grid is initially empty and _A_ will play __first__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
<strong>Output:</strong> "A"
<strong>Explanation:</strong> "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "<strong>X</strong>  "
"   " -&gt; "   " -&gt; " X " -&gt; " X " -&gt; " <strong>X</strong> "
"   "    "O  "    "O  "    "OO "    "OO<strong>X</strong>"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
<strong>Output:</strong> "B"
<strong>Explanation:</strong> "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XX<strong>O</strong>"
"   " -&gt; " O " -&gt; " O " -&gt; " O " -&gt; "XO " -&gt; "X<strong>O</strong> " 
"   "    "   "    "   "    "   "    "   "    "<strong>O</strong>  "
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
<strong>Output:</strong> "Draw"
<strong>Explanation:</strong> The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> moves = [[0,0],[1,1]]
<strong>Output:</strong> "Pending"
<strong>Explanation:</strong> The game has not finished yet.
"X  "
" O "
"   "
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= moves.length &lt;= 9 ``
*   `` moves[i].length == 2 ``
*   `` 0 &lt;= moves[i][j] &lt;= 2 ``
*   There are no repeated elements on `` moves ``.
*   `` moves `` follow the rules of tic tac toe.