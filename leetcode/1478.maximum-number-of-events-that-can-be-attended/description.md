Given an array of `` events `` where <code>events[i] = [startDay<sub>i</sub>, endDay<sub>i</sub>]</code>. Every event `` i `` starts at&nbsp;<code>startDay<sub>i</sub></code><sub>&nbsp;</sub>and ends at&nbsp;<code>endDay<sub>i</sub></code>.

You can attend an event `` i ``&nbsp;at any day&nbsp;`` d `` where&nbsp;<code>startTime<sub>i</sub>&nbsp;&lt;= d &lt;= endTime<sub>i</sub></code>. Notice that you can only attend one event at any time `` d ``.

Return _the maximum number of events&nbsp;_you can attend.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/05/e1.png" style="width: 660px; height: 440px;"/>

<pre>
<strong>Input:</strong> events = [[1,2],[2,3],[3,4]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> events= [[1,2],[2,3],[3,4],[1,2]]
<strong>Output:</strong> 4
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
<strong>Output:</strong> 4
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> events = [[1,100000]]
<strong>Output:</strong> 1
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
<strong>Output:</strong> 7
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= events.length &lt;= 10<sup>5</sup></code>
*   `` events[i].length == 2 ``
*   <code>1 &lt;= startDay<sub>i</sub> &lt;= endDay<sub>i</sub> &lt;= 10<sup>5</sup></code>