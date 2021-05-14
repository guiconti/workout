On an __8x8__ chessboard, there can be multiple Black Queens and one White King.

Given an array of integer coordinates `` queens `` that represents the positions of the Black Queens, and a pair of coordinates `` king `` that represent the position of the White King, return the coordinates of all the queens (in any order) that can attack the King.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/10/01/untitled-diagram.jpg" style="width: 321px; height: 321px;"/>

<pre>
<strong>Input:</strong> queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
<strong>Output:</strong> [[0,1],[1,0],[3,3]]
<strong>Explanation:</strong>&nbsp; 
The queen at [0,1] can attack the king cause they're in the same row. 
The queen at [1,0] can attack the king cause they're in the same column. 
The queen at [3,3] can attack the king cause they're in the same diagnal. 
The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1]. 
The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0]. 
The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/10/01/untitled-diagram-1.jpg" style="width: 321px; height: 321px;"/></strong>

<pre>
<strong>Input:</strong> queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
<strong>Output:</strong> [[2,2],[3,4],[4,4]]
</pre>

__Example 3:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/10/01/untitled-diagram-2.jpg" style="width: 321px; height: 321px;"/></strong>

<pre>
<strong>Input:</strong> queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
<strong>Output:</strong> [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= queens.length&nbsp;&lt;= 63 ``
*   `` queens[i].length == 2 ``
*   `` 0 &lt;= queens[i][j] &lt;&nbsp;8 ``
*   `` king.length == 2 ``
*   `` 0 &lt;= king[0], king[1] &lt; 8 ``
*   At most one piece is allowed in a cell.