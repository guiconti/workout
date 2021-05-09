In a deck of cards, each card has an integer written on it.

Return `` true `` if and only if you can choose `` X &gt;= 2 `` such that it is possible to split the entire deck into 1 or more groups of cards, where:

*   Each group has exactly `` X `` cards.
*   All the cards in each group have the same integer.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> deck = [1,2,3,4,4,3,2,1]
<strong>Output:</strong> true
<strong>Explanation</strong>: Possible partition [1,1],[2,2],[3,3],[4,4].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> deck = [1,1,1,2,2,2,3,3]
<strong>Output:</strong> false
<strong>Explanation</strong>: No possible partition.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> deck = [1]
<strong>Output:</strong> false
<strong>Explanation</strong>: No possible partition.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> deck = [1,1]
<strong>Output:</strong> true
<strong>Explanation</strong>: Possible partition [1,1].
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> deck = [1,1,2,2,2,2]
<strong>Output:</strong> true
<strong>Explanation</strong>: Possible partition [1,1],[2,2],[2,2].
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= deck.length &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= deck[i] &lt; 10<sup>4</sup></code>