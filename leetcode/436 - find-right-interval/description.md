You are given an array of&nbsp;`` intervals ``, where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>&nbsp;and each <code>start<sub>i</sub></code>&nbsp;is __unique__.

The __r____ight____&nbsp;interval__&nbsp;for an interval `` i `` is an interval&nbsp;`` j ``&nbsp;such that <code>start<sub>j</sub></code><code>&nbsp;&gt;= end<sub>i</sub></code>&nbsp;and&nbsp;<code>start<sub>j</sub></code>&nbsp;is&nbsp;__minimized__.

Return&nbsp;_an array of&nbsp;__right interval__&nbsp;indices for each interval&nbsp;`` i ``_. If no&nbsp;__right interval__&nbsp;exists for interval&nbsp;`` i ``, then put&nbsp;`` -1 ``&nbsp;at index `` i ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> intervals = [[1,2]]
<strong>Output:</strong> [-1]
<strong>Explanation:</strong> There is only one interval in the collection, so it outputs -1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> intervals = [[3,4],[2,3],[1,2]]
<strong>Output:</strong> [-1,0,1]
<strong>Explanation:</strong> There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start<sub>0</sub>&nbsp;= 3 is the smallest start that is &gt;= end<sub>1</sub>&nbsp;= 3.
The right interval for [1,2] is [2,3] since start<sub>1</sub>&nbsp;= 2 is the smallest start that is &gt;= end<sub>2</sub>&nbsp;= 2.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> intervals = [[1,4],[2,3],[3,4]]
<strong>Output:</strong> [-1,2,-1]
<strong>Explanation:</strong> There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start<sub>2</sub> = 3 is the smallest start that is &gt;= end<sub>1</sub>&nbsp;= 3.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;=&nbsp;intervals.length &lt;= 2 * 10<sup>4</sup></code>
*   `` intervals[i].length == 2 ``
*   <code>-10<sup>6</sup> &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>6</sup></code>
*   The start point&nbsp;of each interval is __unique__.