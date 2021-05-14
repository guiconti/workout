Given words `` first `` and `` second ``, consider occurrences in some&nbsp;`` text `` of the form "`` first second third ``", where `` second `` comes immediately after `` first ``, and `` third `` comes immediately after `` second ``.

For each such occurrence, add "`` third ``" to the answer, and return the answer.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>text = <span id="example-input-1-1">"alice is a good girl she is a good student"</span>, first = <span id="example-input-1-2">"a"</span>, second = <span id="example-input-1-3">"good"</span>
<strong>Output: </strong><span id="example-output-1">["girl","student"]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>text = <span id="example-input-2-1">"we will we will rock you"</span>, first = <span id="example-input-2-2">"we"</span>, second = <span id="example-input-2-3">"will"</span>
<strong>Output: </strong><span id="example-output-2">["we","rock"]</span>
</pre>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= text.length &lt;= 1000</code></li>
<li><code>text</code> consists of space separated words, where each word consists of lowercase English letters.</li>
<li><code>1 &lt;= first.length, second.length &lt;= 10</code></li>
<li><code>first</code> and <code>second</code> consist of lowercase English letters.</li>
</ol>
</div>