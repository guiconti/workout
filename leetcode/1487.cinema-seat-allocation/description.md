<img alt="" src="https://assets.leetcode.com/uploads/2020/02/14/cinema_seats_1.png" style="width: 400px; height: 149px;"/>

A cinema&nbsp;has `` n ``&nbsp;rows of seats, numbered from 1 to `` n ``&nbsp;and there are ten&nbsp;seats in each row, labelled from 1&nbsp;to 10&nbsp;as shown in the figure above.

Given the array `` reservedSeats `` containing the numbers of seats already reserved, for example, `` reservedSeats[i] = [3,8] ``&nbsp;means the seat located in row __3__ and labelled with __8__&nbsp;is already reserved.

_Return the maximum number of four-person groups&nbsp;you can assign on the cinema&nbsp;seats._ A four-person group&nbsp;occupies four&nbsp;adjacent seats __in one single row__. Seats across an aisle (such as \[3,3\]&nbsp;and \[3,4\]) are not considered to be adjacent, but there is an exceptional case&nbsp;on which an aisle split&nbsp;a four-person group, in that case, the aisle split&nbsp;a four-person group in the middle,&nbsp;which means to have two people on each side.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/14/cinema_seats_3.png" style="width: 400px; height: 96px;"/>

<pre>
<strong>Input:</strong> n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The figure above shows the optimal allocation for four groups, where seats mark with blue are already reserved and contiguous seats mark with orange are for one group.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
<strong>Output:</strong> 2
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 10^9 ``
*   `` 1 &lt;=&nbsp;reservedSeats.length &lt;= min(10*n, 10^4) ``
*   `` reservedSeats[i].length == 2 ``
*   `` 1&nbsp;&lt;=&nbsp;reservedSeats[i][0] &lt;= n ``
*   `` 1 &lt;=&nbsp;reservedSeats[i][1] &lt;= 10 ``
*   All `` reservedSeats[i] `` are distinct.