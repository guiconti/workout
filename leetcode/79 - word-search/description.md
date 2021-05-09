Given an `` m x n `` grid of characters `` board `` and a string `` word ``, return `` true `` _if_ `` word `` _exists in the grid_.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" style="width: 322px; height: 242px;"/>

<pre>
<strong>Input:</strong> board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
<strong>Output:</strong> true
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" style="width: 322px; height: 242px;"/>

<pre>
<strong>Input:</strong> board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
<strong>Output:</strong> true
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/word3.jpg" style="width: 322px; height: 242px;"/>

<pre>
<strong>Input:</strong> board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` m == board.length ``
*   `` n = board[i].length ``
*   `` 1 &lt;= m, n &lt;= 6 ``
*   `` 1 &lt;= word.length &lt;= 15 ``
*   `` board `` and `` word `` consists of only lowercase and uppercase English letters.

&nbsp;

__Follow up:__ Could you use search pruning to make your solution faster with a larger `` board ``?