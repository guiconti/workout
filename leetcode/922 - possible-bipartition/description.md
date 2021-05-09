Given a set of `` N ``&nbsp;people (numbered `` 1, 2, ..., N ``), we would like to split everyone into two groups of __any__ size.

Each person may dislike some other people, and they should not go into the same group.&nbsp;

Formally, if `` dislikes[i] = [a, b] ``, it means it is not allowed to put the people numbered `` a `` and `` b `` into the same group.

Return `` true ``&nbsp;if and only if it is possible to split everyone into two groups in this way.

&nbsp;

<div>
<div>
<ol>
</ol>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong>N = <span id="example-input-1-1">4</span>, dislikes = <span id="example-input-1-2">[[1,2],[1,3],[2,4]]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation</strong>: group1 [1,4], group2 [2,3]
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>N = <span id="example-input-2-1">3</span>, dislikes = <span id="example-input-2-2">[[1,2],[1,3],[2,3]]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong>N = <span id="example-input-3-1">5</span>, dislikes = <span id="example-input-3-2">[[1,2],[2,3],[3,4],[4,5],[1,5]]</span>
<strong>Output: </strong><span id="example-output-3">false</span>
</pre>
</div>
</div>
</div>

&nbsp;

__Constraints:__

*   `` 1 &lt;= N &lt;= 2000 ``
*   `` 0 &lt;= dislikes.length &lt;= 10000 ``
*   `` dislikes[i].length == 2 ``
*   `` 1 &lt;= dislikes[i][j] &lt;= N ``
*   `` dislikes[i][0] &lt; dislikes[i][1] ``
*   There does not exist `` i != j `` for which `` dislikes[i] == dislikes[j] ``.