You are given `` n `` `` points `` in the plane that are all __distinct__, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>. A __boomerang__ is a tuple of points `` (i, j, k) `` such that the distance between `` i `` and `` j `` equals the distance between `` i `` and `` k `` __(the order of the tuple matters)__.

Return _the number of boomerangs_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> points = [[0,0],[1,0],[2,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> points = [[1,1],[2,2],[3,3]]
<strong>Output:</strong> 2
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> points = [[1,1]]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` n == points.length ``
*   `` 1 &lt;= n &lt;= 500 ``
*   `` points[i].length == 2 ``
*   <code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code>
*   All the points are __unique__.