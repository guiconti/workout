Storekeeper is a&nbsp;game&nbsp;in which the player pushes boxes around in a warehouse&nbsp;trying to get them to target locations.

The game is represented by a `` grid `` of size&nbsp;`` m x n ``, where each element is a wall, floor, or a box.

Your task is move the box `` 'B' `` to the target position `` 'T' `` under the following rules:

*   Player is represented by character `` 'S' ``&nbsp;and&nbsp;can move up, down, left, right in the `` grid `` if it is a floor (empy cell).
*   Floor is represented by character `` '.' `` that means free cell to walk.
*   Wall is represented by character `` '#' `` that means obstacle&nbsp;&nbsp;(impossible to walk there).&nbsp;
*   There is only one box `` 'B' `` and one&nbsp;target cell `` 'T' `` in the `` grid ``.
*   The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a __push__.
*   The player cannot walk through the box.

Return the minimum number of __pushes__ to move the box to the target. If there is no way to reach the target, return&nbsp;`` -1 ``.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/11/06/sample_1_1620.png" style="width: 520px; height: 386px;"/></strong>

<pre>
<strong>Input:</strong> grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
&nbsp;              ["#",".",".","B",".","#"],
&nbsp;              ["#",".","#","#",".","#"],
&nbsp;              ["#",".",".",".","S","#"],
&nbsp;              ["#","#","#","#","#","#"]]
<strong>Output:</strong> 3
<strong>Explanation: </strong>We return only the number of times the box is pushed.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
&nbsp;              ["#",".",".","B",".","#"],
&nbsp;              ["#","#","#","#",".","#"],
&nbsp;              ["#",".",".",".","S","#"],
&nbsp;              ["#","#","#","#","#","#"]]
<strong>Output:</strong> -1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> grid = [["#","#","#","#","#","#"],
&nbsp;              ["#","T",".",".","#","#"],
&nbsp;              ["#",".","#","B",".","#"],
&nbsp;              ["#",".",".",".",".","#"],
&nbsp;              ["#",".",".",".","S","#"],
&nbsp;              ["#","#","#","#","#","#"]]
<strong>Output:</strong> 5
<strong>Explanation:</strong>  push the box down, left, left, up and up.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> grid = [["#","#","#","#","#","#","#"],
&nbsp;              ["#","S","#",".","B","T","#"],
&nbsp;              ["#","#","#","#","#","#","#"]]
<strong>Output:</strong> -1
</pre>

&nbsp;

__Constraints:__

<ul><li><code>m ==&nbsp;grid.length</code></li><li><code>n ==&nbsp;grid[i].length</code></li><li><code>1 &lt;= m &lt;= 20</code></li><li><code>1 &lt;= n &lt;= 20</code></li><li><code>grid</code> contains only characters&nbsp;<code>'.'</code>, <code>'#'</code>,&nbsp; <code>'S'</code> , <code>'T'</code>,&nbsp;or <code>'B'</code>.</li><li>There is only one character&nbsp;<code>'S'</code>, <code>'B'</code>&nbsp;<font face="sans-serif, Arial, Verdana, Trebuchet MS">and&nbsp;</font><code>'T'</code>&nbsp;in the <code>grid</code>.</li></ul>