Every non-negative integer `` N ``&nbsp;has a binary representation.&nbsp; For example,&nbsp;`` 5 `` can be represented as `` "101" ``&nbsp;in binary, `` 11 `` as `` "1011" ``&nbsp;in binary, and so on.&nbsp; Note that except for `` N = 0 ``, there are no leading zeroes in any&nbsp;binary representation.

The _complement_&nbsp;of a binary representation&nbsp;is the number in binary you get when changing every `` 1 `` to a `` 0 `` and `` 0 `` to a `` 1 ``.&nbsp; For example, the complement of `` "101" `` in binary is `` "010" `` in binary.

For a given number `` N `` in base-10, return the complement of it's binary representation as a&nbsp;base-10 integer.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-1-1">5</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">7</span>
<strong>Output: </strong><span id="example-output-2">0</span>
<span id="example-output-1"><strong>Explanation: </strong>7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
</span></pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-3-1">10</span>
<strong>Output: </strong><span id="example-output-3">5</span>
<strong>Explanation: </strong>10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
</pre>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ol>
<li><code>0 &lt;= N &lt; 10^9</code></li>
<li>This question is the same as 476:&nbsp;<a href="https://leetcode.com/problems/number-complement/">https://leetcode.com/problems/number-complement/</a></li>
</ol>
</div>
</div>
</div>