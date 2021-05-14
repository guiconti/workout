You are given an array of integers `` distance ``.

You start at point `` (0,0) `` on an __X-Y__ plane and you move `` distance[0] `` meters to the north, then `` distance[1] `` meters to the west, `` distance[2] `` meters to the south, `` distance[3] `` meters to the east, and so on. In other words, after each move, your direction changes counter-clockwise.

Return `` true `` if your path crosses itself, and `` false `` if it does not.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/selfcross1-plane.jpg" style="width: 400px; height: 435px;"/>

<pre>
<strong>Input:</strong> distance = [2,1,1,2]
<strong>Output:</strong> true
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/selfcross2-plane.jpg" style="width: 400px; height: 435px;"/>

<pre>
<strong>Input:</strong> distance = [1,2,3,4]
<strong>Output:</strong> false
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/selfcross3-plane.jpg" style="width: 400px; height: 435px;"/>

<pre>
<strong>Input:</strong> distance = [1,1,1,1]
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;=&nbsp;distance.length &lt;= 500 ``
*   `` 1 &lt;=&nbsp;distance[i] &lt;= 500 ``

&nbsp;

__Follow up:__ Could you write a one-pass algorithm with `` O(1) `` extra space?