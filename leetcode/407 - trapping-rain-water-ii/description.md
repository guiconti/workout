Given an `` m x n `` integer matrix `` heightMap `` representing the height of each unit cell in a 2D elevation map, return _the volume of water it can trap after raining_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/trap1-3d.jpg" style="width: 361px; height: 321px;"/>

<pre>
<strong>Input:</strong> heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> After the rain, water is trapped between the blocks.
We have two small pounds 1 and 3 units trapped.
The total volume of water trapped is 4.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/trap2-3d.jpg" style="width: 401px; height: 321px;"/>

<pre>
<strong>Input:</strong> heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
<strong>Output:</strong> 10
</pre>

&nbsp;

__Constraints:__

*   `` m == heightMap.length ``
*   `` n == heightMap[i].length ``
*   `` 1 &lt;= m, n &lt;= 200 ``
*   <code>0 &lt;= heightMap[i][j] &lt;= 2 * 10<sup>4</sup></code>