You are given an array `` routes `` representing bus routes where `` routes[i] `` is a bus route that the <code>i<sup>th</sup></code> bus repeats forever.

*   For example, if `` routes[0] = [1, 5, 7] ``, this means that the <code>0<sup>th</sup></code> bus travels in the sequence `` 1 -&gt; 5 -&gt; 7 -&gt; 1 -&gt; 5 -&gt; 7 -&gt; 1 -&gt; ... `` forever.

You will start at the bus stop `` source `` (You are not on any bus initially), and you want to go to the bus stop `` target ``. You can travel between bus stops by buses only.

Return _the least number of buses you must take to travel from _`` source ``_ to _`` target ``. Return `` -1 `` if it is not possible.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> routes = [[1,2,7],[3,6,7]], source = 1, target = 6
<strong>Output:</strong> 2
<strong>Explanation:</strong> The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
<strong>Output:</strong> -1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= routes.length &lt;= 500 ``.
*   <code>1 &lt;= routes[i].length &lt;= 10<sup>5</sup></code>
*   All the values of `` routes[i] `` are __unique__.
*   <code>sum(routes[i].length) &lt;= 10<sup>5</sup></code>
*   <code>0 &lt;= routes[i][j] &lt; 10<sup>6</sup></code>
*   <code>0 &lt;= source, target &lt; 10<sup>6</sup></code>