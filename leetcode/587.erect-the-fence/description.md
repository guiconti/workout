You are given an array `` trees `` where <code>trees[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if __all the trees are enclosed__.

Return _the coordinates of trees that are exactly located on the fence perimeter_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/erect2-plane.jpg" style="width: 509px; height: 500px;"/>

<pre>
<strong>Input:</strong> points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
<strong>Output:</strong> [[1,1],[2,0],[3,3],[2,4],[4,2]]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/erect1-plane.jpg" style="width: 509px; height: 500px;"/>

<pre>
<strong>Input:</strong> points = [[1,2],[2,2],[4,2]]
<strong>Output:</strong> [[4,2],[2,2],[1,2]]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= points.length &lt;= 3000 ``
*   `` points[i].length == 2 ``
*   <code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 100</code>
*   All the given points are __unique__.