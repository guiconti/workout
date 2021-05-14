You are given a network of `` n `` nodes, labeled from `` 1 `` to `` n ``. You are also given `` times ``, a list of travel times as directed edges <code>times[i] = (u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>)</code>, where <code>u<sub>i</sub></code> is the source node, <code>v<sub>i</sub></code> is the target node, and <code>w<sub>i</sub></code> is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `` k ``. Return the time it takes for all the `` n `` nodes to receive the signal. If it is impossible for all the `` n `` nodes to receive the signal, return `` -1 ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png" style="width: 217px; height: 239px;"/>

<pre>
<strong>Input:</strong> times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
<strong>Output:</strong> 2
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> times = [[1,2,1]], n = 2, k = 1
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> times = [[1,2,1]], n = 2, k = 2
<strong>Output:</strong> -1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= k &lt;= n &lt;= 100 ``
*   `` 1 &lt;= times.length &lt;= 6000 ``
*   `` times[i].length == 3 ``
*   <code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code>
*   <code>u<sub>i</sub> != v<sub>i</sub></code>
*   <code>0 &lt;= w<sub>i</sub> &lt;= 100</code>
*   All the pairs <code>(u<sub>i</sub>, v<sub>i</sub>)</code> are __unique__. (i.e., no multiple edges.)