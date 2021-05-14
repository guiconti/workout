Given an array of integers `` A ``, find the number of&nbsp;triples of indices (i, j, k)&nbsp;such that:

*   `` 0 &lt;= i &lt; A.length ``
*   `` 0 &lt;= j &lt; A.length ``
*   `` 0 &lt;= k &lt; A.length ``
*   `` A[i]&nbsp;&amp; A[j]&nbsp;&amp; A[k] == 0 ``, where `` &amp; ``&nbsp;represents the bitwise-AND operator.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong><span id="example-input-1-1">[2,1,3]</span>
<strong>Output: </strong><span id="example-output-1">12</span>
<strong>Explanation: </strong>We could choose the following i, j, k triples:
(i=0, j=0, k=1) : 2 &amp; 2 &amp; 1
(i=0, j=1, k=0) : 2 &amp; 1 &amp; 2
(i=0, j=1, k=1) : 2 &amp; 1 &amp; 1
(i=0, j=1, k=2) : 2 &amp; 1 &amp; 3
(i=0, j=2, k=1) : 2 &amp; 3 &amp; 1
(i=1, j=0, k=0) : 1 &amp; 2 &amp; 2
(i=1, j=0, k=1) : 1 &amp; 2 &amp; 1
(i=1, j=0, k=2) : 1 &amp; 2 &amp; 3
(i=1, j=1, k=0) : 1 &amp; 1 &amp; 2
(i=1, j=2, k=0) : 1 &amp; 3 &amp; 2
(i=2, j=0, k=1) : 3 &amp; 2 &amp; 1
(i=2, j=1, k=0) : 3 &amp; 1 &amp; 2
</pre>

&nbsp;

__Note:__

<ol><li><code><font face="monospace">1 &lt;= A.length &lt;= 1000</font></code></li><li><code>0 &lt;= A[i] &lt; 2^16</code></li></ol>