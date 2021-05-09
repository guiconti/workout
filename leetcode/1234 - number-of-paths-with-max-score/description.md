You are given a square `` board ``&nbsp;of characters. You can move on the board starting at the bottom right square marked with the character&nbsp;`` 'S' ``.

You need&nbsp;to reach the top left square marked with the character `` 'E' ``. The rest of the squares are labeled either with a numeric character&nbsp;`` 1, 2, ..., 9 `` or with an obstacle `` 'X' ``. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, __taken modulo `` 10^9 + 7 ``__.

In case there is no path, return&nbsp;`` [0, 0] ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> board = ["E23","2X2","12S"]
<strong>Output:</strong> [7,1]
</pre>

__Example 2:__

<pre><strong>Input:</strong> board = ["E12","1X1","21S"]
<strong>Output:</strong> [4,2]
</pre>

__Example 3:__

<pre><strong>Input:</strong> board = ["E11","XXX","11S"]
<strong>Output:</strong> [0,0]
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= board.length == board[i].length &lt;= 100 ``