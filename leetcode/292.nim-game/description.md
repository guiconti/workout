You are playing the following Nim Game with your friend:

*   Initially, there is a heap of stones on the table.
*   You and your friend will alternate taking turns, and __you go first__.
*   On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
*   The one who removes the last stone is the winner.

Given `` n ``, the number of stones in the heap, return `` true ``_ if you can win the game assuming both you and your friend play optimally, otherwise return _`` false ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> false
<strong>Explanation:</strong> These are the possible outcomes:
1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
In all outcomes, your friend wins.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code>