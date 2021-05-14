There are&nbsp;`` n ``&nbsp;computers numbered from&nbsp;`` 0 ``&nbsp;to&nbsp;`` n-1 ``&nbsp;connected by&nbsp;ethernet cables&nbsp;`` connections ``&nbsp;forming a network where&nbsp;`` connections[i] = [a, b] ``&nbsp;represents a connection between computers&nbsp;`` a ``&nbsp;and&nbsp;`` b ``. Any computer&nbsp;can reach any other computer directly or indirectly through the network.

Given an initial computer network `` connections ``. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the _minimum number of times_ you need to do this in order to make all the computers connected. If it's not possible, return -1.&nbsp;

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/01/02/sample_1_1677.png" style="width: 570px; height: 167px;"/></strong>

<pre>
<strong>Input:</strong> n = 4, connections = [[0,1],[0,2],[1,2]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Remove cable between computer 1 and 2 and place between computers 1 and 3.
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/01/02/sample_2_1677.png" style="width: 660px; height: 167px;"/></strong>

<pre>
<strong>Input:</strong> n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
<strong>Output:</strong> 2
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There are not enough cables.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 10^5 ``
*   `` 1 &lt;= connections.length &lt;= min(n*(n-1)/2, 10^5) ``
*   `` connections[i].length == 2 ``
*   `` 0 &lt;= connections[i][0], connections[i][1]&nbsp;&lt; n ``
*   `` connections[i][0] != connections[i][1] ``
*   There are no repeated connections.
*   No two computers are connected by more than one cable.