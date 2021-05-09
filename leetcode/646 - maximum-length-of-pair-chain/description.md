You are given an array of `` n `` pairs `` pairs `` where <code>pairs[i] = [left<sub>i</sub>, right<sub>i</sub>]</code> and <code>left<sub>i</sub> &lt; right<sub>i</sub></code>.

A pair `` p2 = [c, d] `` __follows__ a pair `` p1 = [a, b] `` if `` b &lt; c ``. A __chain__ of pairs can be formed in this fashion.

Return _the length longest chain which can be formed_.

You do not need to use up all the given intervals. You can select pairs in any order.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> pairs = [[1,2],[2,3],[3,4]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest chain is [1,2] -&gt; [3,4].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> pairs = [[1,2],[7,8],[4,5]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest chain is [1,2] -&gt; [4,5] -&gt; [7,8].
</pre>

&nbsp;

__Constraints:__

*   `` n == pairs.length ``
*   `` 1 &lt;= n &lt;= 1000 ``
*   <code>-1000 &lt;= left<sub>i</sub> &lt; right<sub>i</sub> &lt; 1000</code>