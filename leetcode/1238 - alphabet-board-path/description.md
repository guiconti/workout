On an alphabet board, we start at position `` (0, 0) ``, corresponding to character&nbsp;`` board[0][0] ``.

Here, `` board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"] ``, as shown in the diagram below.

<img alt="" src="https://assets.leetcode.com/uploads/2019/07/28/azboard.png" style="width: 250px; height: 317px;"/>

We may make the following moves:

*   `` 'U' `` moves our position up one row, if the position exists on the board;
*   `` 'D' `` moves our position down one row, if the position exists on the board;
*   `` 'L' `` moves our position left one column, if the position exists on the board;
*   `` 'R' `` moves our position right one column, if the position exists on the board;
*   `` '!' ``&nbsp;adds the character `` board[r][c] `` at our current position `` (r, c) ``&nbsp;to the&nbsp;answer.

(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to `` target ``&nbsp;in the minimum number of moves.&nbsp; You may return any path that does so.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> target = "leet"
<strong>Output:</strong> "DDR!UURRR!!DDD!"
</pre>

__Example 2:__

<pre><strong>Input:</strong> target = "code"
<strong>Output:</strong> "RR!DDRR!UUL!R!"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= target.length &lt;= 100 ``
*   `` target `` consists only of English lowercase letters.