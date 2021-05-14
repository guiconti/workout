There are `` n `` cities numbered from `` 0 `` to `` n-1 ``. Given the array `` edges `` where <code>edges[i] = [from<sub>i</sub>, to<sub>i</sub>, weight<sub>i</sub>]</code> represents a bidirectional and weighted edge between cities <code>from<sub>i</sub></code> and <code>to<sub>i</sub></code>, and given the integer `` distanceThreshold ``.

Return the city with the smallest number of cities that are reachable through some path and whose distance is __at most__ `` distanceThreshold ``, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities ___i___ and ___j___ is equal to the sum of the edges' weights along that path.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/16/find_the_city_01.png" style="width: 300px; height: 225px;"/>

<pre>
<strong>Input:</strong> n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
<strong>Output:</strong> 3
<strong>Explanation: </strong>The figure above describes the graph.&nbsp;
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -&gt; [City 1, City 2]&nbsp;
City 1 -&gt; [City 0, City 2, City 3]&nbsp;
City 2 -&gt; [City 0, City 1, City 3]&nbsp;
City 3 -&gt; [City 1, City 2]&nbsp;
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/16/find_the_city_02.png" style="width: 300px; height: 225px;"/>

<pre>
<strong>Input:</strong> n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
<strong>Output:</strong> 0
<strong>Explanation: </strong>The figure above describes the graph.&nbsp;
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -&gt; [City 1]&nbsp;
City 1 -&gt; [City 0, City 4]&nbsp;
City 2 -&gt; [City 3, City 4]&nbsp;
City 3 -&gt; [City 2, City 4]
City 4 -&gt; [City 1, City 2, City 3]&nbsp;
The city 0 has 1 neighboring city at a distanceThreshold = 2.
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= n &lt;= 100 ``
*   `` 1 &lt;= edges.length &lt;= n * (n - 1) / 2 ``
*   `` edges[i].length == 3 ``
*   <code>0 &lt;= from<sub>i</sub> &lt; to<sub>i</sub> &lt; n</code>
*   <code>1 &lt;= weight<sub>i</sub>,&nbsp;distanceThreshold &lt;= 10^4</code>
*   All pairs <code>(from<sub>i</sub>, to<sub>i</sub>)</code> are distinct.