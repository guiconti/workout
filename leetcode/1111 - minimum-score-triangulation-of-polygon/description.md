You have a convex `` n ``-sided polygon where each vertex has an integer value. You are given an integer array `` values `` where `` values[i] `` is the value of the <code>i<sup>th</sup></code> vertex (i.e., __clockwise order__).

You will __triangulate__ the polygon into `` n - 2 `` triangles. For each triangle, the value of that triangle is the product of the values of its vertices, and the total score of the triangulation is the sum of these values over all `` n - 2 `` triangles in the triangulation.

Return _the smallest possible total score that you can achieve with some triangulation of the polygon_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/shape1.jpg" style="width: 201px; height: 133px;"/>

<pre>
<strong>Input:</strong> values = [1,2,3]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The polygon is already triangulated, and the score of the only triangle is 6.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/shape2.jpg" style="width: 446px; height: 163px;"/>

<pre>
<strong>Input:</strong> values = [3,7,4,5]
<strong>Output:</strong> 144
<strong>Explanation:</strong> There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
The minimum score is 144.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/shape3.jpg" style="width: 207px; height: 163px;"/>

<pre>
<strong>Input:</strong> values = [1,3,1,4,1,5]
<strong>Output:</strong> 13
<strong>Explanation:</strong> The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.
</pre>

&nbsp;

__Constraints:__

*   `` n == values.length ``
*   `` 3 &lt;= n &lt;= 50 ``
*   `` 1 &lt;= values[i] &lt;= 100 ``