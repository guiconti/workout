You are given two jugs with capacities `` jug1Capacity `` and `` jug2Capacity `` liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly `` targetCapacity `` liters using these two jugs.

If `` targetCapacity `` liters of water are measurable, you must have `` targetCapacity `` liters of water contained __within one or both buckets__ by the end.

Operations allowed:

*   Fill any of the jugs with water.
*   Empty any of the jugs.
*   Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> The famous <a href="https://www.youtube.com/watch?v=BVtQNK_ZUJg&amp;ab_channel=notnek01" target="_blank">Die Hard</a> example 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= jug1Capacity, jug2Capacity, targetCapacity &lt;= 10<sup>6</sup></code>