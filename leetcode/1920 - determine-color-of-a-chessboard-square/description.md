You are given `` coordinates ``, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/screenshot-2021-02-20-at-22159-pm.png" style="width: 400px; height: 396px;"/>

Return `` true ``_ if the square is white, and _`` false ``_ if the square is black_.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> coordinates = "a1"
<strong>Output:</strong> false
<strong>Explanation:</strong> From the chessboard above, the square with coordinates "a1" is black, so return false.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> coordinates = "h3"
<strong>Output:</strong> true
<strong>Explanation:</strong> From the chessboard above, the square with coordinates "h3" is white, so return true.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> coordinates = "c7"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` coordinates.length == 2 ``
*   `` 'a' &lt;= coordinates[0] &lt;= 'h' ``
*   `` '1' &lt;= coordinates[1] &lt;= '8' ``