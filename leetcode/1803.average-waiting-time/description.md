There is a restaurant with a single chef. You are given an array `` customers ``, where <code>customers[i] = [arrival<sub>i</sub>, time<sub>i</sub>]:</code>

*   <code>arrival<sub>i</sub></code> is the arrival time of the <code>i<sup>th</sup></code> customer. The arrival times are sorted in __non-decreasing__ order.
*   <code>time<sub>i</sub></code> is the time needed to prepare the order of the <code>i<sup>th</sup></code> customer.

When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers __in the order they were given in the input__.

Return _the __average__ waiting time of all customers_. Solutions within <code>10<sup>-5</sup></code> from the actual answer are considered accepted.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> customers = [[1,2],[2,5],[4,3]]
<strong>Output:</strong> 5.00000
<strong>Explanation:
</strong>1) The first customer arrives at time 1, the chef takes his order and starts preparing it immediately at time 1, and finishes at time 3, so the waiting time of the first customer is 3 - 1 = 2.
2) The second customer arrives at time 2, the chef takes his order and starts preparing it at time 3, and finishes at time 8, so the waiting time of the second customer is 8 - 2 = 6.
3) The third customer arrives at time 4, the chef takes his order and starts preparing it at time 8, and finishes at time 11, so the waiting time of the third customer is 11 - 4 = 7.
So the average waiting time = (2 + 6 + 7) / 3 = 5.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> customers = [[5,2],[5,4],[10,3],[20,1]]
<strong>Output:</strong> 3.25000
<strong>Explanation:
</strong>1) The first customer arrives at time 5, the chef takes his order and starts preparing it immediately at time 5, and finishes at time 7, so the waiting time of the first customer is 7 - 5 = 2.
2) The second customer arrives at time 5, the chef takes his order and starts preparing it at time 7, and finishes at time 11, so the waiting time of the second customer is 11 - 5 = 6.
3) The third customer arrives at time 10, the chef takes his order and starts preparing it at time 11, and finishes at time 14, so the waiting time of the third customer is 14 - 10 = 4.
4) The fourth customer arrives at time 20, the chef takes his order and starts preparing it immediately at time 20, and finishes at time 21, so the waiting time of the fourth customer is 21 - 20 = 1.
So the average waiting time = (2 + 6 + 4 + 1) / 4 = 3.25.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= customers.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= arrival<sub>i</sub>, time<sub>i</sub> &lt;= 10<sup>4</sup></code>
*   <code>arrival<sub>i&nbsp;</sub>&lt;= arrival<sub>i+1</sub></code>