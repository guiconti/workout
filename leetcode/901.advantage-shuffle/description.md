Given two arrays `` A `` and `` B `` of equal size, the _advantage of `` A `` with respect to `` B ``_ is the number of indices `` i ``&nbsp;for which `` A[i] &gt; B[i] ``.

Return __any__ permutation of `` A `` that maximizes its advantage with respect to `` B ``.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[2,7,11,15]</span>, B = <span id="example-input-1-2">[1,10,4,11]</span>
<strong>Output: </strong><span id="example-output-1">[2,11,7,15]</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[12,24,8,32]</span>, B = <span id="example-input-2-2">[13,25,32,11]</span>
<strong>Output: </strong><span id="example-output-2">[24,32,8,12]</span>
</pre>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= A.length = B.length &lt;= 10000</code></li>
<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
<li><code>0 &lt;= B[i] &lt;= 10^9</code></li>
</ol>
</div>
</div>