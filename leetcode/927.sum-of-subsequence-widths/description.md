Given an array of integers `` A ``, consider all non-empty subsequences of `` A ``.

For any sequence S, let the&nbsp;_width_&nbsp;of S be the difference between the maximum and minimum element of S.

Return the sum of the widths of all subsequences of A.&nbsp;

As the answer may be very large, __return the answer modulo 10^9 + 7__.

<div>
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[2,1,3]</span>
<strong>Output: </strong><span id="example-output-1">6</span>
<strong>Explanation:
</strong>Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.
</pre>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ul>
<li><code>1 &lt;= A.length &lt;= 20000</code></li>
<li><code>1 &lt;= A[i] &lt;= 20000</code></li>
</ul>
</div>