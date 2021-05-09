You are given an array `` prices `` where `` prices[i] `` is the price of a given stock on the <code>i<sup>th</sup></code> day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

*   After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

__Note:__ You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> prices = [1,2,3,0,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> transactions = [buy, sell, cooldown, buy, sell]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> prices = [1]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= prices.length &lt;= 5000 ``
*   `` 0 &lt;= prices[i] &lt;= 1000 ``