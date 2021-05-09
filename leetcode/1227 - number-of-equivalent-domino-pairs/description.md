Given a list of `` dominoes ``,&nbsp;`` dominoes[i] = [a, b] ``&nbsp;is _equivalent_ to `` dominoes[j] = [c, d] ``&nbsp;if and only if either (`` a==c `` and `` b==d ``), or (`` a==d `` and `` b==c ``) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs `` (i, j) `` for which `` 0 &lt;= i &lt; j &lt; dominoes.length ``, and&nbsp;`` dominoes[i] `` is equivalent to `` dominoes[j] ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> dominoes = [[1,2],[2,1],[3,4],[5,6]]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= dominoes.length &lt;= 40000 ``
*   `` 1 &lt;= dominoes[i][j] &lt;= 9 ``