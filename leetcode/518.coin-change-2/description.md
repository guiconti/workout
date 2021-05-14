You are given an integer array `` coins `` representing coins of different denominations and an integer `` amount `` representing a total amount of money.

Return _the number of combinations that make up that amount_. If that amount of money cannot be made up by any combination of the coins, return `` 0 ``.

You may assume that you have an infinite number of each kind of coin.

The answer is __guaranteed__ to fit into a signed __32-bit__ integer.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> amount = 5, coins = [1,2,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> amount = 3, coins = [2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> the amount of 3 cannot be made up just with coins of 2.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> amount = 10, coins = [10]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= coins.length &lt;= 300 ``
*   `` 1 &lt;= coins[i] &lt;= 5000 ``
*   `` 0 &lt;= amount &lt;= 5000 ``