You are given an array `` prices `` where `` prices[i] `` is the price of a given stock on the <code>i<sup>th</sup></code> day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

__Note:__ You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> prices = [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e., max profit = 0.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= prices.length &lt;= 3 * 10<sup>4</sup></code>
*   <code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code>