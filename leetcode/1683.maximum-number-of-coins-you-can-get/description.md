There are 3n&nbsp;piles of coins of&nbsp;varying size, you and your friends will take piles of coins as follows:

*   In each step, you will choose __any&nbsp;__3 piles of coins (not necessarily consecutive).
*   Of your choice,&nbsp;Alice&nbsp;will pick&nbsp;the pile with the maximum number of coins.
*   You will pick the next pile with maximum number of coins.
*   Your friend Bob will pick the last pile.
*   Repeat&nbsp;until&nbsp;there are no more piles of coins.

Given an array of integers `` piles ``&nbsp;where `` piles[i] `` is the number of coins in the <code>i<sup>th</sup></code> pile.

Return the maximum number of coins which you can have.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> piles = [2,4,1,2,7,8]
<strong>Output:</strong> 9
<strong>Explanation: </strong>Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with <strong>7</strong> coins and Bob the last one.
Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with <strong>2</strong> coins and Bob the last one.
The maximum number of coins which you can have are: 7 + 2 = 9.
On the other hand if we choose this arrangement (1, <strong>2</strong>, 8), (2, <strong>4</strong>, 7) you only get 2 + 4 = 6 coins which is not optimal.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> piles = [2,4,5]
<strong>Output:</strong> 4
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> piles = [9,8,7,6,5,1,2,3,4]
<strong>Output:</strong> 18
</pre>

&nbsp;

__Constraints:__

*   `` 3 &lt;= piles.length &lt;= 10^5 ``
*   `` piles.length % 3 == 0 ``
*   `` 1 &lt;= piles[i] &lt;= 10^4 ``