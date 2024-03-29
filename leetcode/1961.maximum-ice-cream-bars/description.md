It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are `` n `` ice cream bars. You are given an array `` costs `` of length `` n ``, where `` costs[i] `` is the price of the <code>i<sup>th</sup></code> ice cream bar in coins. The boy initially has `` coins `` coins to spend, and he wants to buy as many ice cream bars as possible.&nbsp;

Return _the __maximum__ number of ice cream bars the boy can buy with _`` coins ``_ coins._

__Note:__ The boy can buy the ice cream bars in any order.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> costs = [1,3,2,4,1], coins = 7
<strong>Output:</strong> 4
<strong>Explanation: </strong>The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> costs = [10,6,8,7,7,8], coins = 5
<strong>Output:</strong> 0
<strong>Explanation: </strong>The boy cannot afford any of the ice cream bars.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> costs = [1,6,3,1,2,5], coins = 20
<strong>Output:</strong> 6
<strong>Explanation: </strong>The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
</pre>

&nbsp;

__Constraints:__

*   `` costs.length == n ``
*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= costs[i] &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= coins &lt;= 10<sup>8</sup></code>