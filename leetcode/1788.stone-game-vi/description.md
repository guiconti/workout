Alice and Bob take turns playing a game, with Alice starting first.

There are `` n `` stones in a pile. On each player's turn, they can __remove__ a stone from the pile and receive points based on the stone's value. Alice and Bob may __value the stones differently__.

You are given two integer arrays of length `` n ``, `` aliceValues `` and `` bobValues ``. Each `` aliceValues[i] `` and `` bobValues[i] `` represents how Alice and Bob, respectively, value the <code>i<sup>th</sup></code> stone.

The winner is the person with the most points after all the stones are chosen. If both players have the same amount of points, the game results in a draw. Both players will play __optimally__.&nbsp;Both players know the other's values.

Determine the result of the game, and:

*   If Alice wins, return `` 1 ``.
*   If Bob wins, return `` -1 ``.
*   If the game results in a draw, return `` 0 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> aliceValues = [1,3], bobValues = [2,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
If Alice takes stone 1 (0-indexed) first, Alice will receive 3 points.
Bob can only choose stone 0, and will only receive 2 points.
Alice wins.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> aliceValues = [1,2], bobValues = [3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
If Alice takes stone 0, and Bob takes stone 1, they will both have 1 point.
Draw.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> aliceValues = [2,4,3], bobValues = [1,6,7]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
Regardless of how Alice plays, Bob will be able to have more points than Alice.
For example, if Alice takes stone 1, Bob can take stone 2, and Alice takes stone 0, Alice will have 6 points to Bob's 7.
Bob wins.
</pre>

&nbsp;

__Constraints:__

*   `` n == aliceValues.length == bobValues.length ``
*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>
*   `` 1 &lt;= aliceValues[i], bobValues[i] &lt;= 100 ``