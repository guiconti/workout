Given an array&nbsp;`` A `` of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list __(including duplicates)__.&nbsp;&nbsp;For example, if a character occurs 3 times&nbsp;in all strings but not 4 times, you need to include that character three times&nbsp;in the final answer.

You may return the answer in any order.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-1-1">["bella","label","roller"]</span>
<strong>Output: </strong><span id="example-output-1">["e","l","l"]</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">["cool","lock","cook"]</span>
<strong>Output: </strong><span id="example-output-2">["c","o"]</span>
</pre>
<p>&nbsp;</p>
<p><strong><span>Note:</span></strong></p>
<ol>
<li><code>1 &lt;= A.length &lt;= 100</code></li>
<li><code>1 &lt;= A[i].length &lt;= 100</code></li>
<li><code>A[i][j]</code> is a lowercase letter</li>
</ol>
</div>
</div>