You are given an array&nbsp;`` coordinates ``, `` coordinates[i] = [x, y] ``, where `` [x, y] `` represents the coordinate of a point. Check if these points&nbsp;make a straight line in the XY plane.

&nbsp;
&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/10/15/untitled-diagram-2.jpg" style="width: 336px; height: 336px;"/>

<pre>
<strong>Input:</strong> coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
<strong>Output:</strong> true
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/10/09/untitled-diagram-1.jpg" style="width: 348px; height: 336px;"/></strong>

<pre>
<strong>Input:</strong> coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;=&nbsp;coordinates.length &lt;= 1000 ``
*   `` coordinates[i].length == 2 ``
*   `` -10^4 &lt;=&nbsp;coordinates[i][0],&nbsp;coordinates[i][1] &lt;= 10^4 ``
*   `` coordinates ``&nbsp;contains no duplicate point.