You are given an array representing a row of `` seats `` where `` seats[i] = 1 `` represents a person sitting in the <code>i<sup>th</sup></code> seat, and `` seats[i] = 0 `` represents that the <code>i<sup>th</sup></code> seat is empty __(0-indexed)__.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.&nbsp;

Return _that maximum distance to the closest person_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/10/distance.jpg" style="width: 650px; height: 257px;"/>

<pre>
<strong>Input:</strong> seats = [1,0,0,0,1,0,1]
<strong>Output:</strong> 2
<strong>Explanation: </strong>
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> seats = [1,0,0,0]
<strong>Output:</strong> 3
<strong>Explanation: </strong>
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> seats = [0,1]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= seats.length &lt;= 2 * 10<sup>4</sup></code>
*   `` seats[i] ``&nbsp;is `` 0 `` or&nbsp;`` 1 ``.
*   At least one seat is __empty__.
*   At least one seat is __occupied__.