Given an `` m x n `` `` board ``&nbsp;of characters and a list of strings `` words ``, return _all words on the board_.

Each word must be constructed from letters of sequentially adjacent cells, where __adjacent cells__ are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/07/search1.jpg" style="width: 322px; height: 322px;"/>

<pre>
<strong>Input:</strong> board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
<strong>Output:</strong> ["eat","oath"]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/07/search2.jpg" style="width: 162px; height: 162px;"/>

<pre>
<strong>Input:</strong> board = [["a","b"],["c","d"]], words = ["abcb"]
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   `` m == board.length ``
*   `` n == board[i].length ``
*   `` 1 &lt;= m, n &lt;= 12 ``
*   `` board[i][j] `` is a lowercase English letter.
*   <code>1 &lt;= words.length &lt;= 3 * 10<sup>4</sup></code>
*   `` 1 &lt;= words[i].length &lt;= 10 ``
*   `` words[i] `` consists of lowercase English letters.
*   All the strings of `` words `` are unique.