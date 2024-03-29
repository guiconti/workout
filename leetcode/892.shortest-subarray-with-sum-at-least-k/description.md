Return the __length__ of the shortest, non-empty, contiguous&nbsp;subarray of `` A `` with sum at least `` K ``.

If there is no non-empty subarray with sum at least `` K ``, return `` -1 ``.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1]</span>, K = <span id="example-input-1-2">1</span>
<strong>Output: </strong><span id="example-output-1">1</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[1,2]</span>, K = <span id="example-input-2-2">4</span>
<strong>Output: </strong><span id="example-output-2">-1</span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[2,-1,2]</span>, K = <span id="example-input-3-2">3</span>
<strong>Output: </strong><span id="example-output-3">3</span>
</pre>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= A.length &lt;= 50000</code></li>
<li><code>-10 ^ 5&nbsp;&lt;= A[i] &lt;= 10 ^ 5</code></li>
<li><code>1 &lt;= K &lt;= 10 ^ 9</code></li>
</ol>
</div>
</div>
</div>