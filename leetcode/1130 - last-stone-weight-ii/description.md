You are given an array of integers `` stones `` where `` stones[i] `` is the weight of the <code>i<sup>th</sup></code> stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights `` x `` and `` y `` with `` x &lt;= y ``. The result of this smash is:

*   If `` x == y ``, both stones are destroyed, and
*   If `` x != y ``, the stone of weight `` x `` is destroyed, and the stone of weight `` y `` has new weight `` y - x ``.

At the end of the game, there is __at most one__ stone left.

Return _the smallest possible weight of the left stone_. If there are no stones left, return `` 0 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> stones = [2,7,4,1,8,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> stones = [31,26,33,21,40]
<strong>Output:</strong> 5
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> stones = [1,2]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= stones.length &lt;= 30 ``
*   `` 1 &lt;= stones[i] &lt;= 100 ``