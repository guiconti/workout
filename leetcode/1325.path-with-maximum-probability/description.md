You are given an undirected weighted graph of&nbsp;`` n ``&nbsp;nodes (0-indexed), represented by an edge list where&nbsp;`` edges[i] = [a, b] ``&nbsp;is an undirected edge connecting the nodes&nbsp;`` a ``&nbsp;and&nbsp;`` b ``&nbsp;with a probability of success of traversing that edge&nbsp;`` succProb[i] ``.

Given two nodes&nbsp;`` start ``&nbsp;and&nbsp;`` end ``, find the path with the maximum probability of success to go from&nbsp;`` start ``&nbsp;to&nbsp;`` end ``&nbsp;and return its success probability.

If there is no path from&nbsp;`` start ``&nbsp;to&nbsp;`` end ``, __return&nbsp;0__. Your answer will be accepted if it differs from the correct answer by at most __1e-5__.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/20/1558_ex1.png" style="width: 187px; height: 186px;"/></strong>

<pre>
<strong>Input:</strong> n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
<strong>Output:</strong> 0.25000
<strong>Explanation:</strong>&nbsp;There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/20/1558_ex2.png" style="width: 189px; height: 186px;"/></strong>

<pre>
<strong>Input:</strong> n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
<strong>Output:</strong> 0.30000
</pre>

__Example 3:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/20/1558_ex3.png" style="width: 215px; height: 191px;"/></strong>

<pre>
<strong>Input:</strong> n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
<strong>Output:</strong> 0.00000
<strong>Explanation:</strong>&nbsp;There is no path between 0 and 2.
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= n &lt;= 10^4 ``
*   `` 0 &lt;= start, end &lt; n ``
*   `` start != end ``
*   `` 0 &lt;= a, b &lt; n ``
*   `` a != b ``
*   `` 0 &lt;= succProb.length == edges.length &lt;= 2*10^4 ``
*   `` 0 &lt;= succProb[i] &lt;= 1 ``
*   There is at most one edge between every two nodes.