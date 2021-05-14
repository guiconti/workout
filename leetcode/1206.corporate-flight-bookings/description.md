There are `` n `` flights that are labeled from `` 1 `` to `` n ``.

You are given an array of flight bookings `` bookings ``, where <code>bookings[i] = [first<sub>i</sub>, last<sub>i</sub>, seats<sub>i</sub>]</code> represents a booking for flights <code>first<sub>i</sub></code> through <code>last<sub>i</sub></code> (__inclusive__) with <code>seats<sub>i</sub></code> seats reserved for __each flight__ in the range.

Return _an array _`` answer ``_ of length _`` n ``_, where _`` answer[i] ``_ is the total number of seats reserved for flight _`` i ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
<strong>Output:</strong> [10,55,45,25,25]
<strong>Explanation:</strong>
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10  10
Booking 2 reserved:      20  20
Booking 3 reserved:      25  25  25  25
Total seats:         10  55  45  25  25
Hence, answer = [10,55,45,25,25]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> bookings = [[1,2,10],[2,2,15]], n = 2
<strong>Output:</strong> [10,25]
<strong>Explanation:</strong>
Flight labels:        1   2
Booking 1 reserved:  10  10
Booking 2 reserved:      15
Total seats:         10  25
Hence, answer = [10,25]

</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code>
*   <code>1 &lt;= bookings.length &lt;= 2 * 10<sup>4</sup></code>
*   `` bookings[i].length == 3 ``
*   <code>1 &lt;= first<sub>i</sub> &lt;= last<sub>i</sub> &lt;= n</code>
*   <code>1 &lt;= seats<sub>i</sub> &lt;= 10<sup>4</sup></code>