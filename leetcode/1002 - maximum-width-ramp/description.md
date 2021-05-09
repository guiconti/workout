Given an array `` A `` of integers, a _ramp_&nbsp;is a tuple `` (i, j) `` for which `` i &lt; j ``&nbsp;and&nbsp;`` A[i] &lt;= A[j] ``.&nbsp; The width of such a&nbsp;ramp is `` j - i ``.

Find the maximum width of a ramp in `` A ``.&nbsp; If one doesn't exist, return 0.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong><span id="example-input-1-1">[6,0,8,2,1,5]</span>
<strong>Output: </strong><span id="example-output-1">4</span>
<strong>Explanation: </strong>
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">[9,8,1,0,1,9,4,0,4,1]</span>
<strong>Output: </strong><span id="example-output-2">7</span>
<strong>Explanation: </strong>
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
</pre>
</div>

<div>
<div>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ol>
<li><code>2 &lt;= A.length &lt;= 50000</code></li>
<li><code>0 &lt;= A[i] &lt;= 50000</code></li>
</ol>
</div>
</div>

<div>
<div>&nbsp;</div>
</div>