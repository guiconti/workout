An integer interval `` [a, b] `` (for integers `` a &lt; b ``) is a set of all consecutive integers from `` a `` to `` b ``, including `` a `` and `` b ``.

Find the minimum size of a set S such that for every integer interval A in `` intervals ``, the intersection of S with A has a size of at least two.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> intervals = [[1,3],[1,4],[2,5],[3,5]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3],[2,4],[4,5]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> An example of a minimum sized set is {1, 2, 3, 4, 5}.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= intervals.length &lt;= 3000 ``
*   `` intervals[i].length == 2 ``
*   <code>0 &lt;= a<sub>i</sub> &lt;&nbsp;b<sub>i</sub> &lt;= 10<sup>8</sup></code>