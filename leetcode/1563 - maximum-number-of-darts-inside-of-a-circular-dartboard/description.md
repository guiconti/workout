You have a very large square wall and a circular dartboard placed on the wall.&nbsp;You have been challenged to throw darts into the board blindfolded.&nbsp;Darts thrown at the wall are represented as an array of&nbsp;`` points `` on a 2D plane.&nbsp;

Return&nbsp;the maximum number of points that are within or&nbsp;lie&nbsp;on&nbsp;__any__ circular dartboard of radius&nbsp;`` r ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/04/29/sample_1_1806.png" style="width: 186px; height: 159px;"/>

<pre>
<strong>Input:</strong> points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> Circle dartboard with center in (0,0) and radius = 2 contain all points.
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/04/29/sample_2_1806.png" style="width: 224px; height: 183px;"/></strong>

<pre>
<strong>Input:</strong> points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
<strong>Output:</strong> 5
<strong>Explanation:</strong> Circle dartboard with center in (0,4) and radius = 5 contain all points except the point (7,8).
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
<strong>Output:</strong> 1
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= points.length &lt;= 100 ``
*   `` points[i].length == 2 ``
*   `` -10^4 &lt;= points[i][0], points[i][1] &lt;= 10^4 ``
*   `` 1 &lt;= r &lt;= 5000 ``