For a string `` sequence ``, a string `` word `` is __`` k ``-repeating__ if `` word `` concatenated `` k `` times is a substring of `` sequence ``. The `` word ``'s __maximum `` k ``-repeating value__ is the highest value `` k `` where `` word `` is `` k ``-repeating in `` sequence ``. If `` word `` is not a substring of `` sequence ``, `` word ``'s maximum `` k ``-repeating value is `` 0 ``.

Given strings `` sequence `` and `` word ``, return _the __maximum `` k ``-repeating value__ of `` word `` in `` sequence ``_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> sequence = "ababc", word = "ab"
<strong>Output:</strong> 2
<strong>Explanation: </strong>"abab" is a substring in "<u>abab</u>c".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> sequence = "ababc", word = "ba"
<strong>Output:</strong> 1
<strong>Explanation: </strong>"ba" is a substring in "a<u>ba</u>bc". "baba" is not a substring in "ababc".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> sequence = "ababc", word = "ac"
<strong>Output:</strong> 0
<strong>Explanation: </strong>"ac" is not a substring in "ababc". 
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= sequence.length &lt;= 100 ``
*   `` 1 &lt;= word.length &lt;= 100 ``
*   `` sequence `` and `` word ``&nbsp;contains only lowercase English letters.