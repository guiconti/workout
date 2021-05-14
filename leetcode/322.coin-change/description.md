You are given an integer array `` coins `` representing coins of different denominations and an integer `` amount `` representing a total amount of money.

Return _the fewest number of coins that you need to make up that amount_. If that amount of money cannot be made up by any combination of the coins, return `` -1 ``.

You may assume that you have an infinite number of each kind of coin.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> coins = [1,2,5], amount = 11
<strong>Output:</strong> 3
<strong>Explanation:</strong> 11 = 5 + 5 + 1
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> coins = [2], amount = 3
<strong>Output:</strong> -1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> coins = [1], amount = 0
<strong>Output:</strong> 0
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> coins = [1], amount = 1
<strong>Output:</strong> 1
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> coins = [1], amount = 2
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= coins.length &lt;= 12 ``
*   <code>1 &lt;= coins[i] &lt;= 2<sup>31</sup> - 1</code>
*   <code>0 &lt;= amount &lt;= 10<sup>4</sup></code>