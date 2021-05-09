Given a __circular&nbsp;array__&nbsp;__C__ of integers represented by&nbsp;`` A ``, find the maximum possible sum of a non-empty subarray of __C__.

Here, a&nbsp;_circular&nbsp;array_ means the end of the array connects to the beginning of the array.&nbsp; (Formally, `` C[i] = A[i] `` when `` 0 &lt;= i &lt; A.length ``, and `` C[i+A.length] = C[i] ``&nbsp;when&nbsp;`` i &gt;= 0 ``.)

Also, a subarray may only include each element of the fixed buffer `` A `` at most once.&nbsp; (Formally, for a subarray `` C[i], C[i+1], ..., C[j] ``, there does not exist `` i &lt;= k1, k2 &lt;= j `` with `` k1 % A.length&nbsp;= k2 % A.length ``.)

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,-2,3,-2]</span>
<strong>Output: </strong><span id="example-output-1">3
<strong>Explanation: </strong>Subarray [3] has maximum sum 3</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">[5,-3,5]</span>
<strong>Output: </strong><span id="example-output-2">10
</span><span id="example-output-3"><strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [5,5] has maximum sum </span><span>5 + 5 = 10</span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-3-1">[3,-1,2,-1]</span>
<strong>Output: </strong><span id="example-output-3">4
<strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [2,-1,3] has maximum sum </span><span>2 + (-1) + 3 = 4</span>
</pre>
<div>
<p><strong>Example 4:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-4-1">[3,-2,2,-3]</span>
<strong>Output: </strong><span id="example-output-4">3
</span><span id="example-output-3"><strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [3] and [3,-2,2] both have maximum sum </span><span>3</span>
</pre>
<p><strong>Example 5:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-5-1">[-2,-3,-1]</span>
<strong>Output: </strong><span id="example-output-5">-1
</span><span id="example-output-3"><strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [-1] has maximum sum -1</span>
</pre>
<p>&nbsp;</p>
<p><strong>Note: </strong></p>
<ol>
<li><code>-30000 &lt;= A[i] &lt;= 30000</code></li>
<li><code>1 &lt;= A.length &lt;= 30000</code></li>
</ol>
</div>
</div>
</div>
</div>