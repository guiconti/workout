In a country popular for train travel, you&nbsp;have planned some train travelling one year in advance.&nbsp; The days of the year that you will travel is given as an array `` days ``.&nbsp; Each day is an integer from `` 1 `` to `` 365 ``.

Train tickets are sold in 3 different ways:

*   a 1-day pass is sold for `` costs[0] `` dollars;
*   a 7-day pass is sold for `` costs[1] `` dollars;
*   a 30-day pass is sold for `` costs[2] `` dollars.

The passes allow that many days of consecutive travel.&nbsp; For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of `` days ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>days = <span id="example-input-1-1">[1,4,6,7,8,20]</span>, costs = <span id="example-input-1-2">[2,7,15]</span>
<strong>Output: </strong><span id="example-output-1">11</span>
<strong>Explanation: </strong>
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>days = <span id="example-input-2-1">[1,2,3,4,5,6,7,8,9,10,30,31]</span>, costs = <span id="example-input-2-2">[2,7,15]</span>
<strong>Output: </strong><span id="example-output-2">17</span>
<strong>Explanation: </strong>
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
</pre>
<p>&nbsp;</p>
</div>

__Note:__

1.   `` 1 &lt;= days.length &lt;= 365 ``
2.   `` 1 &lt;= days[i] &lt;= 365 ``
3.   `` days `` is in strictly increasing order.
4.   `` costs.length == 3 ``
5.   `` 1 &lt;= costs[i] &lt;= 1000 ``