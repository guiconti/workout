An array is _monotonic_ if it is either monotone increasing or monotone decreasing.

An array `` A `` is monotone increasing if for all `` i &lt;= j ``, `` A[i] &lt;= A[j] ``.&nbsp; An array `` A `` is monotone decreasing if for all `` i &lt;= j ``, `` A[i] &gt;= A[j] ``.

Return `` true `` if and only if the given array `` A `` is monotonic.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,2,3]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">[6,5,4,4]</span>
<strong>Output: </strong><span id="example-output-2">true</span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-3-1">[1,3,2]</span>
<strong>Output: </strong><span id="example-output-3">false</span>
</pre>
<div>
<p><strong>Example 4:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-4-1">[1,2,4,5]</span>
<strong>Output: </strong><span id="example-output-4">true</span>
</pre>
<div>
<p><strong>Example 5:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-5-1">[1,1,1]</span>
<strong>Output: </strong><span id="example-output-5">true</span>
</pre>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= A.length &lt;= 50000</code></li>
<li><code>-100000 &lt;= A[i] &lt;= 100000</code></li>
</ol>
</div>
</div>
</div>
</div>
</div>