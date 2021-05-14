There is a group of `` n `` members, and a list of various crimes they could commit. The <code>i<sup>th</sup></code> crime generates a `` profit[i] `` and requires `` group[i] `` members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a __profitable scheme__ any subset of these crimes that generates at least `` minProfit `` profit, and the total number of members participating in that subset of crimes is at most `` n ``.

Return the number of schemes that can be chosen. Since the answer may be very large, __return it modulo__ <code>10<sup>9</sup> + 7</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 5, minProfit = 3, group = [2,2], profit = [2,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
<strong>Output:</strong> 7
<strong>Explanation:</strong> To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 100 ``
*   `` 0 &lt;= minProfit &lt;= 100 ``
*   `` 1 &lt;= group.length &lt;= 100 ``
*   `` 1 &lt;= group[i] &lt;= 100 ``
*   `` profit.length == group.length ``
*   `` 0 &lt;= profit[i] &lt;= 100 ``