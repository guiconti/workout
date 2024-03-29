We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

<pre>
XX  &lt;- domino

XX  &lt;- "L" tromino
X
</pre>

Given N, how many ways are there to tile a 2 x N board? __Return your answer modulo 10^9 + 7__.

(In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.)

<pre>
<strong>Example:</strong>
<strong>Input:</strong> 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
The five different ways are listed below, different letters indicates different tiles:
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY</pre>

__Note:__

*   N&nbsp; will be in range `` [1, 1000] ``.

&nbsp;