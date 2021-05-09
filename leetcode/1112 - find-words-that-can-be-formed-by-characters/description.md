You are given an array of strings&nbsp;`` words ``&nbsp;and a string&nbsp;`` chars ``.

A string is _good_&nbsp;if&nbsp;it can be formed by&nbsp;characters from `` chars ``&nbsp;(each character&nbsp;can only be used once).

Return the sum of lengths of all good strings in `` words ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>words = <span id="example-input-1-1">["cat","bt","hat","tree"]</span>, chars = <span id="example-input-1-2">"atach"</span>
<strong>Output: </strong><span id="example-output-1">6</span>
<strong>Explanation: </strong>
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
</pre>

__Example 2:__

<pre>
<strong>Input: </strong>words = <span id="example-input-2-1">["hello","world","leetcode"]</span>, chars = <span id="example-input-2-2">"welldonehoneyr"</span>
<strong>Output: </strong><span id="example-output-2">10</span>
<strong>Explanation: </strong>
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
</pre>

&nbsp;

<span>__Note:__</span>

1.   `` 1 &lt;= words.length &lt;= 1000 ``
2.   `` 1 &lt;= words[i].length, chars.length&nbsp;&lt;= 100 ``
3.   All strings contain lowercase English letters only.