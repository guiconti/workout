Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,1],[1,3],[3,1],[3,3],[2,2]]</span>
<strong>Output: </strong><span id="example-output-1">4</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]</span>
<strong>Output: </strong><span id="example-output-2">2</span>
</pre>
<p>&nbsp;</p>
<p><strong>Note</strong>:</p>
<ol>
<li><code>1 &lt;= points.length &lt;= 500</code></li>
<li><code>0 &lt;=&nbsp;points[i][0] &lt;=&nbsp;40000</code></li>
<li><code>0 &lt;=&nbsp;points[i][1] &lt;=&nbsp;40000</code></li>
<li>All points are distinct.</li>
</ol>
</div>
</div>