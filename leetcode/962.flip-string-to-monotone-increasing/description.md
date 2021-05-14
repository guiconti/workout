A string of `` '0' ``s and `` '1' ``s is _monotone increasing_ if it consists of some number of `` '0' ``s (possibly 0), followed by some number of `` '1' ``s (also possibly 0.)

We are given a string `` S `` of `` '0' ``s and `` '1' ``s, and we may flip any `` '0' `` to a `` '1' `` or a `` '1' `` to a `` '0' ``.

Return the minimum number of flips to make `` S ``&nbsp;monotone increasing.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-1-1">"00110"</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>We flip the last digit to get 00111.
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">"010110"</span>
<strong>Output: </strong><span id="example-output-2">2</span>
<strong>Explanation: </strong>We flip to get 011111, or alternatively 000111.
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-3-1">"00011000"</span>
<strong>Output: </strong><span id="example-output-3">2</span>
<strong>Explanation: </strong>We flip to get 00000000.
</pre>
<p>&nbsp;</p>
<p><strong><span>Note:</span></strong></p>
<ol>
<li><code>1 &lt;= S.length &lt;= 20000</code></li>
<li><code>S</code> only consists of <code>'0'</code> and <code>'1'</code> characters.</li>
</ol>
</div>
</div>
</div>