Given an array of `` points `` where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the __X-Y__ plane, return _the maximum number of points that lie on the same straight line_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg" style="width: 300px; height: 294px;"/>

<pre>
<strong>Input:</strong> points = [[1,1],[2,2],[3,3]]
<strong>Output:</strong> 3
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg" style="width: 300px; height: 294px;"/>

<pre>
<strong>Input:</strong> points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= points.length &lt;= 300 ``
*   `` points[i].length == 2 ``
*   <code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code>
*   All the `` points `` are __unique__.