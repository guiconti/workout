You are given an array `` prices `` where `` prices[i] `` is the price of a given stock on the <code>i<sup>th</sup></code> day, and an integer `` fee `` representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

__Note:__ You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> prices = [1,3,2,8,4,9], fee = 2
<strong>Output:</strong> 8
<strong>Explanation:</strong> The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> prices = [1,3,7,5,10,3], fee = 3
<strong>Output:</strong> 6
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= prices.length &lt;= 5 * 10<sup>4</sup></code>
*   <code>1 &lt;= prices[i] &lt; 5 * 10<sup>4</sup></code>
*   <code>0 &lt;= fee &lt; 5 * 10<sup>4</sup></code>