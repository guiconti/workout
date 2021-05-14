We have a two dimensional matrix&nbsp;`` A `` where each value is `` 0 `` or `` 1 ``.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all `` 0 ``s to `` 1 ``s, and all `` 1 ``s to `` 0 ``s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible&nbsp;score.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[[0,0,1,1],[1,0,1,0],[1,1,0,0]]</span>
<strong>Output: </strong><span id="example-output-1">39</span>
<strong>Explanation:
</strong>Toggled to <span id="example-input-1-1">[[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39</span></pre>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= A.length &lt;= 20</code></li>
<li><code>1 &lt;= A[0].length &lt;= 20</code></li>
<li><code>A[i][j]</code>&nbsp;is <code>0</code> or <code>1</code>.</li>
</ol>
</div>