The __n-queens__ puzzle is the problem of placing `` n `` queens on an `` n x n `` chessboard such that no two queens attack each other.

Given an integer `` n ``, return _all distinct solutions to the __n-queens puzzle___.

Each solution contains a distinct board configuration of the n-queens' placement, where `` 'Q' `` and `` '.' `` both indicate a queen and an empty space, respectively.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" style="width: 600px; height: 268px;"/>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
<strong>Explanation:</strong> There exist two distinct solutions to the 4-queens puzzle as shown above
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> [["Q"]]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 9 ``