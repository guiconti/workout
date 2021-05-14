You are given an integer array `` cost `` where `` cost[i] `` is the cost of <code>i<sup>th</sup></code> step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `` 0 ``, or the step with index `` 1 ``.

Return _the minimum cost to reach the top of the floor_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> cost = [10,15,20]
<strong>Output:</strong> 15
<strong>Explanation:</strong> Cheapest is: start on cost[1], pay that cost, and go to the top.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> cost = [1,100,1,1,1,100,1,1,100,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= cost.length &lt;= 1000 ``
*   `` 0 &lt;= cost[i] &lt;= 999 ``