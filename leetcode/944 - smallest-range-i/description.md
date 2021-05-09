Given an array `` A `` of integers, for each integer `` A[i] `` we may choose any `` x `` with `` -K &lt;= x &lt;= K ``, and add `` x `` to `` A[i] ``.

After this process, we have some array `` B ``.

Return the smallest possible difference between the maximum value of `` B ``&nbsp;and the minimum value of `` B ``.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1]</span>, K = <span id="example-input-1-2">0</span>
<strong>Output: </strong><span id="example-output-1">0
<strong>Explanation</strong>: B = [1]</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[0,10]</span>, K = <span id="example-input-2-2">2</span>
<strong>Output: </strong><span id="example-output-2">6
</span><span id="example-output-1"><strong>Explanation</strong>: B = [2,8]</span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[1,3,6]</span>, K = <span id="example-input-3-2">3</span>
<strong>Output: </strong><span id="example-output-3">0
</span><span id="example-output-1"><strong>Explanation</strong>: B = [3,3,3] or B = [4,4,4]</span>
</pre>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= A.length &lt;= 10000</code></li>
<li><code>0 &lt;= A[i] &lt;= 10000</code></li>
<li><code>0 &lt;= K &lt;= 10000</code></li>
</ol>
</div>
</div>
</div>