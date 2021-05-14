Given a set of _non-overlapping_ intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> intervals = [[1,3],[6,9]], newInterval = [2,5]
<strong>Output:</strong> [[1,5],[6,9]]
</pre>

__Example 2:__

<strong>Input:</strong> intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    <strong>Output:</strong> [[1,2],[3,10],[12,16]]
    <strong>Explanation:</strong> Because the new interval [4,8] overlaps with <code>[3,5],[6,7],[8,10]</code>.

__Example 3:__

<pre>
<strong>Input:</strong> intervals = [], newInterval = [5,7]
<strong>Output:</strong> [[5,7]]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> intervals = [[1,5]], newInterval = [2,3]
<strong>Output:</strong> [[1,5]]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> intervals = [[1,5]], newInterval = [2,7]
<strong>Output:</strong> [[1,7]]
</pre>

&nbsp;

__Constraints:__

*   <code>0 &lt;= intervals.length &lt;= 10<sup>4</sup></code>
*   `` intervals[i].length == 2 ``
*   <code>0 &lt;=&nbsp;intervals[i][0] &lt;=&nbsp;intervals[i][1] &lt;= 10<sup>5</sup></code>
*   `` intervals ``&nbsp;is sorted by `` intervals[i][0] `` in __ascending__&nbsp;order.
*   `` newInterval.length == 2 ``
*   <code>0 &lt;=&nbsp;newInterval[0] &lt;=&nbsp;newInterval[1] &lt;= 10<sup>5</sup></code>