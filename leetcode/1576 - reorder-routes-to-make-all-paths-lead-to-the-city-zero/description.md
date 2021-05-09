There are&nbsp;`` n ``&nbsp;cities numbered from&nbsp;`` 0 ``&nbsp;to&nbsp;`` n-1 `` and&nbsp;`` n-1 `` roads such that&nbsp;there is only one way to travel between two&nbsp;different cities (this network form a tree).&nbsp;Last year,&nbsp;The ministry of transport&nbsp;decided to orient the roads in one direction because they are too narrow.

Roads are represented by&nbsp;`` connections ``&nbsp;where&nbsp;`` connections[i] = [a, b] ``&nbsp;represents a&nbsp;road&nbsp;from city&nbsp;`` a ``&nbsp;to&nbsp;`` b ``.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting&nbsp;some roads such that each city can visit the city&nbsp;0. Return the __minimum__ number of edges changed.

It's __guaranteed__ that each city can reach the city 0 after reorder.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/05/13/sample_1_1819.png" style="width: 240px; height: 150px;"/></strong>

<pre>
<strong>Input:</strong> n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
<strong>Output:</strong> 3
<strong>Explanation: </strong>Change the direction of edges show in red such that each node can reach the node 0 (capital).</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/05/13/sample_2_1819.png" style="width: 380px; height: 60px;"/></strong>

<pre>
<strong>Input:</strong> n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
<strong>Output:</strong> 2
<strong>Explanation: </strong>Change the direction of edges show in red such that each node can reach the node 0 (capital).</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 3, connections = [[1,0],[2,0]]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= n &lt;= 5 * 10^4 ``
*   `` connections.length == n-1 ``
*   `` connections[i].length == 2 ``
*   `` 0 &lt;= connections[i][0], connections[i][1] &lt;= n-1 ``
*   `` connections[i][0] != connections[i][1] ``