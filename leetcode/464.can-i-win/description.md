In the "100 game" two players take turns adding, to a running total, any integer from `` 1 `` to `` 10 ``. The player who first causes the running total to __reach or exceed__ 100 wins.

What if we change the game so that players __cannot__ re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total &gt;= 100.

Given two integers `` maxChoosableInteger `` and `` desiredTotal ``, return `` true `` if the first player to move can force a win, otherwise, return `` false ``. Assume both players play __optimally__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> maxChoosableInteger = 10, desiredTotal = 11
<strong>Output:</strong> false
<strong>Explanation:</strong>
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is &gt;= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> maxChoosableInteger = 10, desiredTotal = 0
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> maxChoosableInteger = 10, desiredTotal = 1
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= maxChoosableInteger &lt;= 20 ``
*   `` 0 &lt;= desiredTotal &lt;= 300 ``