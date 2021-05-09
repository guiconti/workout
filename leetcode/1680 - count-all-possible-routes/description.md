You are given an array of __distinct__ positive integers locations&nbsp;where `` locations[i] `` represents the position of city `` i ``. You are also given&nbsp;integers&nbsp;`` start ``,&nbsp;`` finish ``&nbsp;and&nbsp;`` fuel ``&nbsp;representing the starting city, ending city, and the initial amount of fuel you have, respectively.

At each step, if you are at city&nbsp;`` i ``, you can pick any city&nbsp;`` j ``&nbsp;such that `` j != i ``&nbsp;and&nbsp;`` 0 &lt;= j &lt; locations.length ``&nbsp;and move to city `` j ``.&nbsp;Moving from city `` i `` to city `` j `` reduces the amount of fuel you have by&nbsp;`` |locations[i] - locations[j]| ``.&nbsp;Please notice that `` |x| ``&nbsp;denotes the absolute value of `` x ``.

Notice that&nbsp;`` fuel ``&nbsp;__cannot__ become negative at any point in time, and that you are __allowed__ to visit any city more than once (including `` start ``&nbsp;and&nbsp;`` finish ``).

Return _the count of all possible routes from&nbsp;_`` start ``&nbsp;_to_&nbsp;`` finish ``.

Since the answer&nbsp;may be too large,&nbsp;return it modulo&nbsp;`` 10^9 + 7 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
<strong>Output:</strong> 4
<strong>Explanation:</strong>&nbsp;The following are all possible routes, each uses 5 units of fuel:
1 -&gt; 3
1 -&gt; 2 -&gt; 3
1 -&gt; 4 -&gt; 3
1 -&gt; 4 -&gt; 2 -&gt; 3
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> locations = [4,3,1], start = 1, finish = 0, fuel = 6
<strong>Output:</strong> 5
<strong>Explanation: </strong>The following are all possible routes:
1 -&gt; 0, used fuel = 1
1 -&gt; 2 -&gt; 0, used fuel = 5
1 -&gt; 2 -&gt; 1 -&gt; 0, used fuel = 5
1 -&gt; 0 -&gt; 1 -&gt; 0, used fuel = 3
1 -&gt; 0 -&gt; 1 -&gt; 0 -&gt; 1 -&gt; 0, used fuel = 5
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> locations = [5,2,1], start = 0, finish = 2, fuel = 3
<strong>Output:</strong> 0
<b>Explanation: </b>It's impossible to get from 0 to 2 using only 3 units of fuel since the shortest route needs 4 units of fuel.</pre>

__Example 4:__

<pre>
<strong>Input:</strong> locations = [2,1,5], start = 0, finish = 0, fuel = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong>&nbsp;There are two possible routes, 0 and 0 -&gt; 1 -&gt; 0.</pre>

__Example 5:__

<pre>
<strong>Input:</strong> locations = [1,2,3], start = 0, finish = 2, fuel = 40
<strong>Output:</strong> 615088286
<strong>Explanation: </strong>The total number of possible routes is 2615088300. Taking this number modulo 10^9 + 7 gives us 615088286.
</pre>

&nbsp;

__Constraints:__

<ul><li><code>2 &lt;= locations.length &lt;= 100</code></li><li><code>1 &lt;= locations[i] &lt;= 10^9</code></li><li>All integers in&nbsp;<code>locations</code>&nbsp;are&nbsp;<strong>distinct</strong>.</li><li><code>0 &lt;= start, finish &lt;&nbsp;locations.length</code></li><li><code><font face="monospace">1 &lt;= fuel &lt;= 200</font></code></li></ul>