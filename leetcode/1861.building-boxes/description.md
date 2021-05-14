You have a cubic storeroom where the width, length, and height of the room are all equal to `` n `` units. You are asked to place `` n `` boxes in this room where each box is a cube of unit side length. There are however some rules to placing the boxes:

*   You can place the boxes anywhere on the floor.
*   If box `` x `` is placed on top of the box `` y ``, then each side of the four vertical sides of the box `` y `` __must__ either be adjacent to another box or to a wall.

Given an integer `` n ``, return_ the __minimum__ possible number of boxes touching the floor._

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/3-boxes.png" style="width: 135px; height: 143px;"/>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The figure above is for the placement of the three boxes.
These boxes are placed in the corner of the room, where the corner is on the left side.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/4-boxes.png" style="width: 135px; height: 179px;"/>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> The figure above is for the placement of the four boxes.
These boxes are placed in the corner of the room, where the corner is on the left side.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/10-boxes.png" style="width: 271px; height: 257px;"/>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 6
<strong>Explanation:</strong> The figure above is for the placement of the ten boxes.
These boxes are placed in the corner of the room, where the corner is on the back side.</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 10<sup>9</sup></code>