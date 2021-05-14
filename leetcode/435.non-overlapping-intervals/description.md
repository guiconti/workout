Given an array of intervals `` intervals `` where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, return _the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3],[3,4],[1,3]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> [1,3] can be removed and the rest of the intervals are non-overlapping.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> intervals = [[1,2],[1,2],[1,2]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> You need to remove two [1,2] to make the rest of the intervals non-overlapping.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> You don't need to remove any of the intervals since they're already non-overlapping.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= intervals.length &lt;= 2 * 10<sup>4</sup></code>
*   `` intervals[i].length == 2 ``
*   <code>-2 * 10<sup>4</sup> &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 2 * 10<sup>4</sup></code>