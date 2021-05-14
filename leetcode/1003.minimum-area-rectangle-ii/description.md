Given a set of points in the xy-plane, determine the minimum area of __any__ rectangle formed from these points, with sides __not necessarily parallel__ to the x and y axes.

If there isn't any rectangle, return 0.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/21/1a.png" style="width: 150px; height: 151px;"/>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,2],[2,1],[1,0],[0,1]]</span>
<strong>Output: </strong><span id="example-output-1">2.00000
<strong>Explanation:</strong> </span><span>The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>
<p><img alt="" src="https://assets.leetcode.com/uploads/2018/12/22/2.png" style="width: 150px; height: 94px;"/></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">[[0,1],[2,1],[1,1],[1,0],[2,0]]</span>
<strong>Output: </strong><span id="example-output-2">1.00000
</span><strong>Explanation:</strong> The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
</pre>
<div>
<p><strong>Example 3:</strong></p>
<p><img alt="" src="https://assets.leetcode.com/uploads/2018/12/22/3.png" style="width: 160px; height: 167px;"/></p>
<pre>
<strong>Input: </strong><span id="example-input-3-1">[[0,3],[1,2],[3,1],[1,3],[2,1]]</span>
<strong>Output: </strong><span id="example-output-3">0
</span><span><strong>Explanation:</strong> There is no possible rectangle to form from these points.</span>
</pre>
<div>
<p><strong>Example 4:</strong></p>
<p><img alt="" src="https://assets.leetcode.com/uploads/2018/12/21/4c.png" style="width: 160px; height: 155px;"/></p>
<pre>
<strong>Input: </strong><span id="example-input-4-1">[[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]</span>
<strong>Output: </strong><span id="example-output-4">2.00000
</span><span><strong>Explanation:</strong> The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.</span>
</pre>
</div>
<p>&nbsp;</p>
</div>
</div>

__Note:__

1.   `` 1 &lt;= points.length &lt;= 50 ``
2.   `` 0 &lt;=&nbsp;points[i][0] &lt;=&nbsp;40000 ``
3.   `` 0 &lt;=&nbsp;points[i][1] &lt;=&nbsp;40000 ``
4.   All points are distinct.
5.   Answers within `` 10^-5 `` of the actual value will be accepted as correct.