Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number `` n `` on the chalkboard. On each player's turn, that player makes a move consisting of:

*   Choosing any `` x `` with `` 0 &lt; x &lt; n `` and `` n % x == 0 ``.
*   Replacing the number `` n `` on the chalkboard with `` n - x ``.

Also, if a player cannot make a move, they lose the game.

Return `` true `` _if and only if Alice wins the game, assuming both players play optimally_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> Alice chooses 1, and Bob has no more moves.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> false
<strong>Explanation:</strong> Alice chooses 1, Bob chooses 1, and Alice has no more moves.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 1000 ``