Given a string&nbsp;`` S `` of `` '(' `` and `` ')' `` parentheses, we add the minimum number of parentheses ( `` '(' `` or `` ')' ``, and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

*   It is the empty string, or
*   It can be written as `` AB ``&nbsp;(`` A `` concatenated with `` B ``), where `` A `` and `` B `` are valid strings, or
*   It can be written as `` (A) ``, where `` A `` is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong><span id="example-input-1-1">"())"</span>
<strong>Output: </strong><span id="example-output-1">1</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">"((("</span>
<strong>Output: </strong><span id="example-output-2">3</span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-3-1">"()"</span>
<strong>Output: </strong><span id="example-output-3">0</span>
</pre>
<div>
<p><strong>Example 4:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-4-1">"()))(("</span>
<strong>Output: </strong><span id="example-output-4">4</span></pre>
<p>&nbsp;</p>
</div>
</div>
</div>

__Note:__

1.   `` S.length &lt;= 1000 ``
2.   `` S `` only consists of `` '(' `` and `` ')' `` characters.

<div>
<div>
<div>
<div>&nbsp;</div>
</div>
</div>
</div>