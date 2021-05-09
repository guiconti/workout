Alice and Bob continue their&nbsp;games with piles of stones. There are several stones&nbsp;__arranged in a row__, and each stone has an associated&nbsp;value which is an integer given in the array&nbsp;`` stoneValue ``.

Alice and Bob take turns, with __Alice__ starting first. On each player's turn, that player&nbsp;can take __1, 2 or 3 stones__&nbsp;from&nbsp;the __first__ remaining stones in the row.

The score of each player is the sum of values of the stones taken. The score of each player is __0__&nbsp;initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume&nbsp;Alice&nbsp;and Bob&nbsp;__play optimally__.

Return _"Alice"_ if&nbsp;Alice will win, _"Bob"_ if Bob will win or _"Tie"_ if they end the game with the same score.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> values = [1,2,3,7]
<strong>Output:</strong> "Bob"
<strong>Explanation:</strong> Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> values = [1,2,3,-9]
<strong>Output:</strong> "Alice"
<strong>Explanation:</strong> Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. The next move Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. The next move Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> values = [1,2,3,6]
<strong>Output:</strong> "Tie"
<strong>Explanation:</strong> Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> values = [1,2,3,-1,-2,-3,7]
<strong>Output:</strong> "Alice"
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> values = [-1,-2,-3]
<strong>Output:</strong> "Tie"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= values.length &lt;= 50000 ``
*   `` -1000&nbsp;&lt;= values[i] &lt;= 1000 ``