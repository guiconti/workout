Given an array `` points `` where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the __X-Y__ plane, return `` true `` _if these points are a __boomerang___.

A __boomerang__ is a set of three points that are __all distinct__ and __not in a straight line__.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> points = [[1,1],[2,3],[3,2]]
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre><strong>Input:</strong> points = [[1,1],[2,2],[3,3]]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` points.length == 3 ``
*   `` points[i].length == 2 ``
*   <code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 100</code>