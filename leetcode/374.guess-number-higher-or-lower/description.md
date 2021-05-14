We are playing the Guess Game. The game is as follows:

I pick a number from `` 1 `` to `` n ``. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `` int guess(int num) ``, which returns 3 possible results:

*   `` -1 ``: The number I picked is lower than your guess (i.e. `` pick &lt; num ``).
*   `` 1 ``: The number I picked is higher than your guess (i.e. `` pick &gt; num ``).
*   `` 0 ``: The number I picked is equal to your guess (i.e. `` pick == num ``).

Return _the number that I picked_.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> n = 10, pick = 6
<strong>Output:</strong> 6
</pre>

__Example 2:__

<pre><strong>Input:</strong> n = 1, pick = 1
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre><strong>Input:</strong> n = 2, pick = 1
<strong>Output:</strong> 1
</pre>

__Example 4:__

<pre><strong>Input:</strong> n = 2, pick = 2
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code>
*   `` 1 &lt;= pick &lt;= n ``