A string is considered __beautiful__ if it satisfies the following conditions:

*   Each of the 5 English vowels (`` 'a' ``, `` 'e' ``, `` 'i' ``, `` 'o' ``, `` 'u' ``) must appear __at least once__ in it.
*   The letters must be sorted in __alphabetical order__ (i.e. all `` 'a' ``s before `` 'e' ``s, all `` 'e' ``s before `` 'i' ``s, etc.).

For example, strings `` "aeiou" `` and `` "aaaaaaeiiiioou" `` are considered __beautiful__, but `` "uaeio" ``, `` "aeoiu" ``, and `` "aaaeeeooo" `` are __not beautiful__.

Given a string `` word `` consisting of English vowels, return _the __length of the longest beautiful substring__ of _`` word ``_. If no such substring exists, return _`` 0 ``.

A __substring__ is a contiguous sequence of characters in a string.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> word = "aeiaaio<u>aaaaeiiiiouuu</u>ooaauuaeiu"
<strong>Output:</strong> 13
<b>Explanation:</b> The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> word = "aeeeiiiioooauuu<u>aeiou</u>"
<strong>Output:</strong> 5
<b>Explanation:</b> The longest beautiful substring in word is "aeiou" of length 5.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> word = "a"
<strong>Output:</strong> 0
<b>Explanation:</b> There is no beautiful substring, so return 0.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= word.length &lt;= 5 * 10<sup>5</sup></code>
*   `` word `` consists of characters `` 'a' ``, `` 'e' ``, `` 'i' ``, `` 'o' ``, and `` 'u' ``.