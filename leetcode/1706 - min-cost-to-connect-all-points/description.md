You are given an array&nbsp;`` points ``&nbsp;representing integer coordinates of some points on a 2D-plane, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>.

The cost of connecting two points <code>[x<sub>i</sub>, y<sub>i</sub>]</code> and <code>[x<sub>j</sub>, y<sub>j</sub>]</code> is the __manhattan distance__ between them:&nbsp;<code>|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code>, where `` |val| `` denotes the absolute value of&nbsp;`` val ``.

Return&nbsp;_the minimum cost to make all points connected._ All points are connected if there is __exactly one__ simple path between any two points.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/d.png" style="width: 214px; height: 268px;"/>

<pre>
<strong>Input:</strong> points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
<strong>Output:</strong> 20
<strong>Explanation:
</strong><img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/c.png" style="width: 214px; height: 268px;"/>
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> points = [[3,12],[-2,5],[-4,1]]
<strong>Output:</strong> 18
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> points = [[0,0],[1,1],[1,0],[-1,1]]
<strong>Output:</strong> 4
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> points = [[-1000000,-1000000],[1000000,1000000]]
<strong>Output:</strong> 4000000
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> points = [[0,0]]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= points.length &lt;= 1000 ``
*   <code>-10<sup>6</sup>&nbsp;&lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>6</sup></code>
*   All pairs <code>(x<sub>i</sub>, y<sub>i</sub>)</code> are distinct.