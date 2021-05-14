Given a list of `` intervals ``, remove all intervals that are covered by another interval in the list.

Interval `` [a,b) `` is covered by&nbsp;interval `` [c,d) `` if and only if `` c &lt;= a `` and `` b &lt;= d ``.

After doing so, return _the number of remaining intervals_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> intervals = [[1,4],[3,6],[2,8]]
<strong>Output:</strong> 2
<b>Explanation: </b>Interval [3,6] is covered by [2,8], therefore it is removed.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> intervals = [[1,4],[2,3]]
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> intervals = [[0,10],[5,12]]
<strong>Output:</strong> 2
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> intervals = [[3,10],[4,10],[5,11]]
<strong>Output:</strong> 2
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> intervals = [[1,2],[1,4],[3,4]]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= intervals.length &lt;= 1000 ``
*   `` intervals[i].length == 2 ``
*   `` 0 &lt;= intervals[i][0] &lt;&nbsp;intervals[i][1] &lt;= 10^5 ``
*   All the intervals are __unique__.