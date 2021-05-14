Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are `` n `` stones in a pile.&nbsp; On each player's turn, that player makes a&nbsp;_move_&nbsp;consisting of removing __any__ non-zero __square number__ of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive&nbsp;integer `` n ``.&nbsp;Return&nbsp;`` True ``&nbsp;if and only if Alice wins the game otherwise return `` False ``, assuming both players play optimally.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation: </strong>Alice can remove 1 stone winning the game because Bob doesn't have any moves.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> false
<strong>Explanation: </strong>Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -&gt; 1 -&gt; 0).</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> n is already a perfect square, Alice can win with one move, removing 4 stones (4 -&gt; 0).
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> false
<strong>Explanation: </strong>Alice can't win the game if Bob plays optimally.
If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should remove only 1 stone and finally Bob removes the last one (7 -&gt; 3 -&gt; 2 -&gt; 1 -&gt; 0). 
If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only can remove 1 stone and finally Bob removes the last one (7 -&gt; 6 -&gt; 2 -&gt; 1 -&gt; 0).</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 17
<strong>Output:</strong> false
<strong>Explanation: </strong>Alice can't win the game if Bob plays optimally.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 10^5 ``