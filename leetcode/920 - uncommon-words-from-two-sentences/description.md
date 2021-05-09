We are given two sentences `` A `` and `` B ``.&nbsp; (A _sentence_&nbsp;is a string of space separated words.&nbsp; Each _word_ consists only of lowercase letters.)

A word is _uncommon_&nbsp;if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.&nbsp;

You may return the list in any order.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">"this apple is sweet"</span>, B = <span id="example-input-1-2">"this apple is sour"</span>
<strong>Output: </strong><span id="example-output-1">["sweet","sour"]</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">"apple apple"</span>, B = <span id="example-input-2-2">"banana"</span>
<strong>Output: </strong><span id="example-output-2">["banana"]</span>
</pre>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ol>
<li><code>0 &lt;= A.length &lt;= 200</code></li>
<li><code>0 &lt;= B.length &lt;= 200</code></li>
<li><code>A</code> and <code>B</code> both contain only spaces and lowercase letters.</li>
</ol>
</div>
</div>