There are `` n `` servers numbered from `` 0 `` to `` n - 1 `` connected by undirected server-to-server `` connections `` forming a network where <code>connections[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> represents a connection between servers <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code>. Any server can reach other servers directly or indirectly through the network.

A _critical connection_ is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/03/1537_ex1_2.png" style="width: 198px; height: 248px;"/></strong>

<pre>
<strong>Input:</strong> n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
<strong>Output:</strong> [[1,3]]
<strong>Explanation:</strong> [[3,1]] is also accepted.
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= n &lt;= 10<sup>5</sup></code>
*   <code>n - 1 &lt;= connections.length &lt;= 10<sup>5</sup></code>
*   <code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code>
*   <code>a<sub>i</sub> != b<sub>i</sub></code>
*   There are no repeated connections.