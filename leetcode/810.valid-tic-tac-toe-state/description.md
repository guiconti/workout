A Tic-Tac-Toe board is given as a string array `` board ``. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The `` board `` is a 3 x 3 array, and consists of characters `` " " ``, `` "X" ``, and `` "O" ``.&nbsp; The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

*   Players take turns placing characters into empty squares (" ").
*   The first player always places "X" characters, while the second player always places "O" characters.
*   "X" and "O" characters are always placed into empty squares, never filled ones.
*   The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
*   The game also ends if all squares are non-empty.
*   No more moves can be played if the game is over.

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> board = ["O&nbsp; ", "&nbsp; &nbsp;", "&nbsp; &nbsp;"]
<strong>Output:</strong> false
<strong>Explanation:</strong> The first player always plays "X".

<strong>Example 2:</strong>
<strong>Input:</strong> board = ["XOX", " X ", "   "]
<strong>Output:</strong> false
<strong>Explanation:</strong> Players take turns making moves.

<strong>Example 3:</strong>
<strong>Input:</strong> board = ["XXX", "   ", "OOO"]
<strong>Output:</strong> false

<strong>Example 4:</strong>
<strong>Input:</strong> board = ["XOX", "O O", "XOX"]
<strong>Output:</strong> true
</pre>

__Note:__

*   `` board `` is a length-3 array of strings, where each string `` board[i] `` has length 3.
*   Each `` board[i][j] `` is a character in the set `` {" ", "X", "O"} ``.