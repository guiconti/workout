You have an `` inventory `` of different colored balls, and there is a customer that wants `` orders `` balls of __any__ color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls __of that color&nbsp;__you currently have in your `` inventory ``. For example, if you own `` 6 `` yellow balls, the customer would pay `` 6 `` for the first yellow ball. After the transaction, there are only `` 5 `` yellow balls left, so the next yellow ball is then valued at `` 5 `` (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, `` inventory ``, where `` inventory[i] `` represents the number of balls of the <code>i<sup>th</sup></code> color that you initially own. You are also given an integer `` orders ``, which represents the total number of balls that the customer wants. You can sell the balls __in any order__.

Return _the __maximum__ total value that you can attain after selling _`` orders ``_ colored balls_. As the answer may be too large, return it __modulo __<code>10<sup>9 </sup>+ 7</code>.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/jj.gif" style="width: 480px; height: 270px;"/>

<pre>
<strong>Input:</strong> inventory = [2,5], orders = 4
<strong>Output:</strong> 14
<strong>Explanation:</strong> Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> inventory = [3,5], orders = 6
<strong>Output:</strong> 19
<strong>Explanation: </strong>Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> inventory = [2,8,4,10,6], orders = 20
<strong>Output:</strong> 110
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> inventory = [1000000000], orders = 1000000000
<strong>Output:</strong> 21
<strong>Explanation: </strong>Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 10<sup>9 </sup>+ 7 = 21.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= inventory.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= inventory[i] &lt;= 10<sup>9</sup></code>
*   <code>1 &lt;= orders &lt;= min(sum(inventory[i]), 10<sup>9</sup>)</code>