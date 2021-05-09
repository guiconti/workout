There is an infrastructure of `` n `` cities with some number of `` roads `` connecting these cities. Each <code>roads[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is a bidirectional road between cities <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code>.

The __network rank___ _of __two different cities__ is defined as the total number of&nbsp;__directly__ connected roads to __either__ city. If a road is directly connected to both cities, it is only counted __once__.

The __maximal network rank __of the infrastructure is the __maximum network rank__ of all pairs of different cities.

Given the integer `` n `` and the array `` roads ``, return _the __maximal network rank__ of the entire infrastructure_.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/ex1.png" style="width: 292px; height: 172px;"/></strong>

<pre>
<strong>Input:</strong> n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/ex2.png" style="width: 292px; height: 172px;"/></strong>

<pre>
<strong>Input:</strong> n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> There are 5 roads that are connected to cities 1 or 2.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= n &lt;= 100 ``
*   `` 0 &lt;= roads.length &lt;= n * (n - 1) / 2 ``
*   `` roads[i].length == 2 ``
*   <code>0 &lt;= a<sub>i</sub>, b<sub>i</sub>&nbsp;&lt;= n-1</code>
*   <code>a<sub>i</sub>&nbsp;!=&nbsp;b<sub>i</sub></code>
*   Each&nbsp;pair of cities has __at most one__ road connecting them.